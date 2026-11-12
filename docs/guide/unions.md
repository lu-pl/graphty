# Discriminated unions

Real data is often polymorphic: some rows describe cats, some dogs; some payments use cards,
others bank transfers. Pydantic models this with
[discriminated unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions),
and `graphty` supports them directly. The dispatch happens **inside the Polars query plan**,
so every row is shaped for the right model before validation.

!!! warning "Model unions must be discriminated"

    A union of several models needs a discriminator, otherwise `graphty` can't tell which model
    a row belongs to and raises a [`MissingDiscriminatorError`](errors.md#missingdiscriminatorerror).

## String discriminators

The discriminator names a `Literal` field shared by all members:

```python
from typing import Annotated, Literal

class Cat(BaseModel):
    pet_type: Literal["cat"]
    meows: int

class Dog(BaseModel):
    pet_type: Literal["dog"]
    barks: float

class Owner(BaseModel):
    model_config = ConfigDict(group_by="owner")

    owner: str
    pets: list[Annotated[Cat | Dog, Field(discriminator="pet_type")]]
```

```python
rows = [
    {"owner": "Ada", "pet_type": "cat", "meows": 3, "barks": None},
    {"owner": "Ada", "pet_type": "dog", "meows": None, "barks": 1.5},
    {"owner": "Bob", "pet_type": "dog", "meows": None, "barks": 4.0},
]
```

```python
>>> list(ModelMaterializer(model=Owner, data=rows).generate_models())
[
    Owner(owner='Ada', pets=[Cat(pet_type='cat', meows=3), Dog(pet_type='dog', barks=1.5)]),
    Owner(owner='Bob', pets=[Dog(pet_type='dog', barks=4.0)]),
]
```

Multi-value literals such as `Literal["reptile", "lizard"]` and every union spelling
(`A | B`, `Union[A, B]`, `Annotated[...]`, `= Field(discriminator=...)`) are supported.

## Callable discriminators

When no single column decides the type, use a callable `Discriminator` with `Tag`ged
members. `graphty` calls it with each row:

```python
from typing import Any
from pydantic import Discriminator, Tag

class Card(BaseModel):
    number: str

class Iban(BaseModel):
    iban: str

def payment_kind(v: Any) -> str | None:
    if isinstance(v, dict):
        return "card" if v.get("number") else "iban"
    return "card" if isinstance(v, Card) else "iban"

class Payment(BaseModel):
    amount: float
    method: Annotated[
        Annotated[Card, Tag("card")] | Annotated[Iban, Tag("iban")],
        Discriminator(payment_kind),
    ]
```

```python
>>> rows = [
...     {"amount": 9.5, "number": "4111", "iban": None},
...     {"amount": 20.0, "number": None, "iban": "AT61"},
... ]
>>> list(ModelMaterializer(model=Payment, data=rows).generate_models())
[
    Payment(amount=9.5, method=Card(number='4111')),
    Payment(amount=20.0, method=Iban(iban='AT61')),
]
```

!!! tip "Performance"

    String discriminators compile to pure Polars expressions. Callable discriminators run
    Python per row, so prefer string discriminators for large datasets.

Unions can be nested inside each other and combined with grouping at any level.
