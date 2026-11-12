# Getting started

## Installation

`graphty` requires Python 3.12 or newer and is available on [PyPI](https://pypi.org/project/graphty/).

=== "uv"

    ```bash
    uv add graphty
    ```

=== "pip"

    ```bash
    pip install graphty
    ```

=== "poetry"

    ```bash
    poetry add graphty
    ```

## Your first model

Start with flat, tabular data. Here, every row is a point:

```python
data = [
    {"x": 0.0, "y": 0.0},
    {"x": 1.0, "y": 0.0},
    {"x": 0.5, "y": 1.0},
]
```

The simplest case is a single model for a point:

```python
from collections.abc import Iterator

from graphty import ModelMaterializer
from pydantic import BaseModel

class Point(BaseModel):
    x: float
    y: float

points: Iterator[Point] = ModelMaterializer(
    model=Point,
    data=data,
).generate_models()
```

This yields one `Point` per row:

```python
>>> list(points)
[Point(x=0.0, y=0.0), Point(x=1.0, y=0.0), Point(x=0.5, y=1.0)]
```

Admittedly, there is not much for `graphty` to do here yet: the result is the same as calling
`Point.model_validate` on every row. Things get interesting once models are nested and aggregated.

## Nesting and aggregation

Now, every row is one vertex of a named polygon:

```python
data = [
    {"name": "triangle", "x": 0.0, "y": 0.0},
    {"name": "triangle", "x": 1.0, "y": 0.0},
    {"name": "triangle", "x": 0.5, "y": 1.0},
    {"name": "square", "x": 0.0, "y": 0.0},
    {"name": "square", "x": 1.0, "y": 0.0},
    {"name": "square", "x": 1.0, "y": 1.0},
    {"name": "square", "x": 0.0, "y": 1.0},
]
```

A polygon is a named list of points. So `Point` becomes a nested model inside a `Polygon` model:

```python hl_lines="6 9"
from collections.abc import Iterator

from graphty import ConfigDict

class Polygon(BaseModel):
    model_config = ConfigDict(group_by="name")

    name: str
    vertices: list[Point]

polygons: Iterator[Polygon] = ModelMaterializer(
    model=Polygon,
    data=data,
).generate_models()
```

The two highlighted lines are all `graphty` needs:

- `vertices: list[Point]` is an **aggregation target**: every row of a polygon becomes a `Point` in this list.
  `Point` is a model itself, so `graphty` builds it from the row's `x` and `y` columns.
- `group_by="name"` tells `graphty` **which column identifies a polygon**. Any model with a `list` field needs one.

This time, the result is a stream of validated `Polygon` instances. Serialized to JSON, they look like this:

```json
[
    {
        "name": "triangle",
        "vertices": [
            {"x": 0.0, "y": 0.0},
            {"x": 1.0, "y": 0.0},
            {"x": 0.5, "y": 1.0}
        ]
    },
    {
        "name": "square",
        "vertices": [
            {"x": 0.0, "y": 0.0},
            {"x": 1.0, "y": 0.0},
            {"x": 1.0, "y": 1.0},
            {"x": 0.0, "y": 1.0}
        ]
    }
]
```

Models can nest and aggregate other models to any depth: every code path in `graphty` is recursive.

!!! tip "`graphty`'s `ConfigDict`"

    `graphty.ConfigDict` is Pydantic's `ConfigDict` with one extra key, `group_by`.
    Every other Pydantic config option works as usual.
