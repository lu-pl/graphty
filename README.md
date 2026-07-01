<img src="https://raw.githubusercontent.com/lu-pl/graphty/refs/heads/main/graphty.svg" width="50%" height="50%" />

#
![tests](https://github.com/lu-pl/graphty/actions/workflows/tests.yaml/badge.svg)
[![coverage](https://coveralls.io/repos/github/lu-pl/graphty/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/lu-pl/graphty?branch=lupl/actions)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)


`graphty` is a Python library for materializing [Pydantic](https://github.com/pydantic/pydantic) object graphs from relational data.

> WARNING: This project is in an early stage of development and should be used with caution.

## Introduction 

The `graphty` library addresses the *structural* [impedance mismatch](https://en.wikipedia.org/wiki/Object%E2%80%93relational_impedance_mismatch) between flat relational data representations and hierarchical object models. It extends Pydantic with a small declarative DSL for expressing grouping, aggregation, and deduplication operations. These transformations are compiled into [Polars](https://github.com/pola-rs/polars) expressions, yielding records that are subsequently validated and materialized as Pydantic model objects.

Although originally developed for implementing typed REST APIs over SPARQL endpoints, the model materializer can be applied to any tabular data representation, including SQL query results, CSV files, dataframes, etc.


## Installation
`graphty` is a [PEP 621](https://peps.python.org/pep-0621/)-compliant package and available on [PyPI](https://pypi.org/project/graphty/).


## Usage

As mentioned, `graphty` uses Pydantic model definitions as declarative data transformation instructions, extending Pydantic with a small DSL for grouping and aggregation. 

Nested models are resolved recursively, `list` types are interpreted as aggregation targets and require a `group_by` definition in `ConfigDict`.


### Basic Example

Given simple relational Author/Work data

```python
data = [
    {"name": "Tolkien", "title": "The Hobbit", "year": 1937},
    {"name": "Tolkien", "title": "The Lord of the Rings", "year": 1954},
    {"name": "Tolkien", "title": "The Silmarillion", "year": 1977},
    {"name": "Orwell", "title": "Animal Farm", "year": 1945},
    {"name": "Orwell", "title": "1984", "year": 1949},
]
```

one can define and materialize a Pydantic model like so: 

```python
from collections.abc import Iterator
from pydantic import BaseModel
from graphty import ConfigDict, ModelMaterializer

class Work(BaseModel):
    title: str
    year: int

class Author(BaseModel):
    model_config = ConfigDict(group_by="name")

    name: str
    works: list[Work]
 
models: Iterator[Author] = ModelMaterializer(model=Author, data=data).generate_models()
```

Here, the `Author` model defines a model aggregation target for the `Author.works` field; the `graphty` planner will therefore partition the underlying data according to the "name" key and aggregate `Work` objects into a list.

> Note that `graphty` is recursive on all code paths and ergo enables materialization of arbitrarily nested and aggregated object graphs.

The above validates against the `Author` model and serializes to the following JSON representation:

```json
[
    {
        "name": "Tolkien",
        "works": [
            {
                "title": "The Hobbit",
                "year": 1937
            },
            {
                "title": "The Lord of the Rings",
                "year": 1954
            },
            {
                "title": "The Silmarillion",
                "year": 1977
            }
        ]
    },
    {
        "name": "Orwell",
        "works": [
            {
                "title": "Animal Farm",
                "year": 1945
            },
            {
                "title": "1984",
                "year": 1949
            }
        ]
    }
]
```