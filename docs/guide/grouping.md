# Grouping & nesting

`graphty` reads a model hierarchy as a description of how to reshape flat rows. Two ideas
cover most of it: **nested models** and **grouping**.

The examples on this page use this order data:

```python
rows = [
    {"order_id": 1, "customer": "Ada", "city": "London", "item": "Lamp", "qty": 2},
    {"order_id": 1, "customer": "Ada", "city": "London", "item": "Desk", "qty": 1},
    {"order_id": 2, "customer": "Bob", "city": "Vienna", "item": "Lamp", "qty": 5},
]
```

## Nested models

A field typed as another model builds that model from columns **of the same row**.
Without `group_by`, you get one object per row:

```python
class Customer(BaseModel):
    customer: str
    city: str

class OrderLine(BaseModel):
    order_id: int
    buyer: Customer
    item: str
```

```python
>>> [line.model_dump() for line in ModelMaterializer(model=OrderLine, data=rows).generate_models()]
[
    {"order_id": 1, "buyer": {"customer": "Ada", "city": "London"}, "item": "Lamp"},
    {"order_id": 1, "buyer": {"customer": "Ada", "city": "London"}, "item": "Desk"},
    {"order_id": 2, "buyer": {"customer": "Bob", "city": "Vienna"}, "item": "Lamp"},
]
```

## Grouping and aggregation targets

A `list` field is an **aggregation target**: it gathers values from several rows. To know
*which* rows belong together, the model must declare a `group_by` key:

```python hl_lines="10 14"
class Customer(BaseModel):
    customer: str
    city: str

class Line(BaseModel):
    item: str
    qty: int

class Order(BaseModel):
    model_config = ConfigDict(group_by="order_id")

    order_id: int
    buyer: Customer
    lines: list[Line]
    status: str = "open"
```

```python
>>> [order.model_dump() for order in ModelMaterializer(model=Order, data=rows).generate_models()]
[
    {
        "order_id": 1,
        "buyer": {"customer": "Ada", "city": "London"},
        "lines": [{"item": "Lamp", "qty": 2}, {"item": "Desk", "qty": 1}],
        "status": "open",
    },
    {
        "order_id": 2,
        "buyer": {"customer": "Bob", "city": "Vienna"},
        "lines": [{"item": "Lamp", "qty": 5}],
        "status": "open",
    },
]
```

Inside a grouped model:

| Field type                | Default behaviour                                       |
|---------------------------|---------------------------------------------------------|
| scalar (`int`, `str`, …)  | first value of the group, see [`Reduce`](aggregations.md#reduce) |
| model (`Customer`)        | first value of the group                                |
| `list[...]`               | all values of the group, deduplicated and without nulls, see [`Collect`](aggregations.md#collect) |
| column not in the data    | ignored by `graphty`, so Pydantic defaults apply (`status` above) |

!!! info "`group_by` names a field, not a column"

    The grouping key refers to a **model field**. If that field has an
    [alias](aliases.md), `graphty` resolves it to the right column for you.
    It must reference a scalar field, otherwise `graphty` raises an
    [`InvalidGroupByError`](errors.md#invalidgroupbyerror).

## Nesting groups inside groups

Models in a list can have their own `group_by`. `graphty` then groups recursively, one level
per model. This is how the [`Author → Work → genres` example](../why.md#the-graphty-way)
is built:

```python
class Work(BaseModel):
    model_config = ConfigDict(group_by="title")  # one Work per title…

    title: str
    year: int
    genres: list[str] = Field(validation_alias="genre")  # …collecting its genres

class Author(BaseModel):
    model_config = ConfigDict(group_by="name")  # one Author per name…

    name: str = Field(validation_alias="author")
    born: int
    works: list[Work]  # …collecting their works
```

There is no limit to the depth: every code path in the planner is recursive.

!!! tip "Hiding helper keys"

    Sometimes a grouping key is only needed to shape the data, not in the output.
    Use Pydantic's `Field(exclude=True)` to keep it out of `model_dump()`.
