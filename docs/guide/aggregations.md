# Aggregations

Inside a [grouped model](grouping.md), every field has to turn many rows into one value.
`graphty` picks a sensible default, and you can override it per field with an
`Annotated` aggregation.

```python
from typing import Annotated
from graphty import Collect, ConfigDict, Reduce
```

## `Reduce`

`Reduce` collapses a group into a **single value**. It is the default for scalar and model
fields, using `first`.

Pass the name of any [Polars expression method](https://docs.pola.rs/api/python/stable/reference/expressions/index.html),
or a callable taking a `pl.Expr`. Extra keyword arguments are forwarded:

=== "By name"

    ```python hl_lines="6"
    class OrderSummary(BaseModel):
        model_config = ConfigDict(group_by="order_id")

        order_id: int
        item: list[str]
        total: Annotated[int, Reduce("sum")] = Field(validation_alias="qty")
    ```

    ```python
    >>> list(ModelMaterializer(model=OrderSummary, data=rows).generate_models())
    [
        OrderSummary(order_id=1, item=['Lamp', 'Desk'], total=3),
        OrderSummary(order_id=2, item=['Lamp'], total=5),
    ]
    ```

=== "Callable with arguments"

    ```python hl_lines="5"
    class Measurement(BaseModel):
        model_config = ConfigDict(group_by="k")

        k: int
        v: Annotated[float, Reduce(pl.Expr.quantile, quantile=0.5)]
    ```

    ```python
    # rows: {"k": 1, "v": 1}, {"k": 1, "v": 3}, {"k": 1, "v": 10}
    >>> list(ModelMaterializer(model=Measurement, data=rows).generate_models())
    [Measurement(k=1, v=3.0)]
    ```

## `Collect`

`Collect` gathers a group into a **list**. It is the default for `list` fields, and by default
removes duplicates and nulls:

=== "Default"

    ```python
    class M(BaseModel):
        model_config = ConfigDict(group_by="k")

        k: int
        v: list[int]  # same as Annotated[list[int], Collect()]
    ```

    ```python
    # rows: {"k": 1, "v": 2}, {"k": 1, "v": 2}, {"k": 1, "v": None}
    >>> [m.model_dump() for m in ModelMaterializer(model=M, data=rows).generate_models()]
    [{"k": 1, "v": [2]}]
    ```

=== "Keep everything"

    ```python
    class M(BaseModel):
        model_config = ConfigDict(group_by="k")

        k: int
        v: Annotated[list[int | None], Collect(unique=False, drop_nulls=False)]
    ```

    ```python
    # rows: {"k": 1, "v": 2}, {"k": 1, "v": 2}, {"k": 1, "v": None}
    >>> [m.model_dump() for m in ModelMaterializer(model=M, data=rows).generate_models()]
    [{"k": 1, "v": [2, 2, None]}]
    ```

## Custom aggregations

Both are implementations of the small `Aggregation` protocol: a callable from one
`pl.Expr` to another. Subclass it to put any Polars logic behind a readable name:

```python
import polars as pl
from graphty import Aggregation


class Coalesce(Aggregation):
    """First non-null value of the group."""

    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return expr.drop_nulls().first()


class Concatenate(Aggregation):
    """Join all values of the group into one string."""

    def __init__(self, separator: str = ", ") -> None:
        self.separator = separator

    def __call__(self, expr: pl.Expr) -> pl.Expr:
        return expr.drop_nulls().implode().list.join(self.separator)


class Book(BaseModel):
    model_config = ConfigDict(group_by="title")

    title: str
    genre: Annotated[str, Concatenate()]
```

```python
>>> [book.model_dump() for book in ModelMaterializer(model=Book, data=rows).generate_models()]
[
    {"title": "The Hobbit", "genre": "fantasy, children"},
    {"title": "The Lord of the Rings", "genre": "fantasy"},
    ...
]
```

!!! note

    Aggregations run inside the Polars query plan, so even custom ones stay vectorised and fast.
