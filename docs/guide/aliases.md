# Aliases

Column names in the source data rarely match the field names you want in your API.
`graphty` respects Pydantic's **validation aliases**, so you map columns to fields exactly as
you would with plain Pydantic.

## Simple aliases

```python
class Author(BaseModel):
    model_config = ConfigDict(group_by="name")

    name: str = Field(validation_alias="author")  # reads the "author" column
    works: list[Work]
```

`group_by` and the planner work with **field names**. `graphty` resolves the alias to the
column behind it.

## Alias choices

`AliasChoices` lets one model accept data from differently named sources. `graphty` picks the
**first** choice that exists as a column:

```python
from pydantic import AliasChoices

class Resource(BaseModel):
    name: str = Field(validation_alias=AliasChoices("name", "label", "rdfs_label"))
```

```python
>>> list(ModelMaterializer(model=Resource, data=[{"rdfs_label": "x"}]).generate_models())
[Resource(name='x')]
```

If none of the choices is present, `graphty` raises an
[`AliasResolutionError`](errors.md#aliasresolutionerror) that tells you what it looked for.

## Validating by name

Pydantic's `validate_by_name` and `validate_by_alias` flags are honoured. With both
enabled, the field name itself also counts as a candidate:

```python
class Resource(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    name: str = Field(validation_alias="label")
```

```python
>>> list(ModelMaterializer(model=Resource, data=[{"name": "x"}]).generate_models())
[Resource(name='x')]
```

## Limitations

- `AliasPath` is not supported. Nested paths make no sense for flat rows, so `graphty`
  raises `NotImplementedError`.
- The deprecated `populate_by_name` flag is rejected. Use `validate_by_name` /
  `validate_by_alias` (Pydantic ≥ 2.11) instead.
- Each column can feed only one field per model. Two fields aliased to the same column
  are currently not supported.
