---
hide:
  - navigation
  - toc
---

<div class="gt-hero" markdown>

<img class="gt-hero__logo" src="assets/graphty-wordmark.svg" alt="Graph[T]">

# Flat tables in. Typed object graphs out.

`graphty` turns flat rows from SQL, SPARQL, CSV or any dataframe into nested, validated [Pydantic](https://docs.pydantic.dev) objects.

You describe the shape, `graphty` builds it.

[Why `graphty`?](why.md){ .md-button .md-button--primary }
[Get started](getting-started.md){ .md-button }

</div>

<div class="gt-example" markdown>

<div markdown>

<p class="gt-caption">Flat data and a model</p>

```python
import json

from pydantic import BaseModel
from graphty import ConfigDict, ModelMaterializer


rows = [
    {"name": "Tolkien", "title": "The Hobbit", "year": 1937},
    {"name": "Tolkien", "title": "The Lord of the Rings", "year": 1954},
    {"name": "Tolkien", "title": "The Silmarillion", "year": 1977},
    {"name": "Orwell", "title": "Animal Farm", "year": 1945},
    {"name": "Orwell", "title": "1984", "year": 1949},
]


class Work(BaseModel):
    title: str
    year: int


class Author(BaseModel):
    model_config = ConfigDict(group_by="name")

    name: str
    works: list[Work]


authors = ModelMaterializer(model=Author, data=rows).generate_models()
print(json.dumps([author.model_dump() for author in authors], indent=4))
```

</div>

<div markdown>

<p class="gt-caption">The result, serialized as JSON</p>

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

</div>

</div>
