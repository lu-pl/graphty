# Errors

`graphty` checks your models while planning and raises descriptive errors for specifications it
can't turn into a query. All of them are importable from `graphty`. Data that doesn't fit the
models raises Pydantic's usual `ValidationError` in `generate_models()`.

## `MissingGroupByError`

A model has a `list` field but no `group_by` key, so `graphty` can't know which rows belong together.

```python
class Author(BaseModel):
    name: str
    works: list[Work]  # aggregation target without group_by
```

```text
MissingGroupByError: Model 'Author' with aggregation target does not specify ConfigDict.group_by.
```

**Fix:** add `model_config = ConfigDict(group_by="name")`.

## `InvalidGroupByError`

The grouping key points at something that isn't a scalar field, such as a list or a nested model.

```text
InvalidGroupByError: Invalid grouping key 'lines' for 'Order'. Grouping keys must reference scalar model fields.
```

## `MissingDiscriminatorError`

A field is a union of several models without a discriminator.

```text
MissingDiscriminatorError: Multi-Model unions must be discriminated unions. Unable to extract discriminator for union type 'pets.Cat | pets.Dog'.
```

**Fix:** see [Discriminated unions](unions.md).

## `AliasResolutionError`

None of a field's `AliasChoices` exists as a column in the data.

```text
AliasResolutionError: Unable to resolve AliasChoice for field 'name' of model 'Resource': None of computed aliases '['name', 'label', 'rdfs_label']' in input data projection '{'other'}'.
```

**Fix:** check the column names of your data, or add the missing choice.
