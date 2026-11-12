# Opaque fields

Sometimes a field needs logic that doesn't fit the declarative model: combining several
columns, parsing a format, calling a lookup. Mark it `Opaque` and `graphty` steps aside.
The field receives the **whole raw row** as a dict, and a Pydantic `before` validator can
build the value in Python.

```python hl_lines="7"
from typing import Annotated
from pydantic import field_validator
from graphty import Opaque

class Book(BaseModel):
    title: str
    summary: Annotated[str, Opaque()]

    @field_validator("summary", mode="before")
    @classmethod
    def build_summary(cls, row: dict) -> str:
        return f"{row['title']} ({row['year']}) by {row['author']}"
```

```python
>>> next(ModelMaterializer(model=Book, data=rows).generate_models())
Book(title='The Hobbit', summary='The Hobbit (1937) by Tolkien')
```

## Opaque fields in groups

In a grouped model, an opaque field receives **all raw rows of the group** as a list.
Opaque fields of a nested, non-list model in a grouped parent see the first row of the group.

!!! tip "Use sparingly"

    Opaque fields run in Python, outside the Polars plan. They are an escape hatch:
    reach for [aggregations](aggregations.md) first, since they stay in the fast path.
