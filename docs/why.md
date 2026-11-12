# Why `graphty`?

## The problem

Databases, triple stores and data files hand you **flat rows**. Applications and APIs want
**nested objects**. Every row repeats its parents' data, and someone has to write code that
groups, deduplicates and nests it back into shape.

That code is tedious, easy to get subtly wrong, and has to be kept in sync with the API models
by hand. Developers call this the
[object–relational impedance mismatch](https://en.wikipedia.org/wiki/Object%E2%80%93relational_impedance_mismatch).

## The `graphty` way

With `graphty`, the model you already write for validation and your API **is** the
transformation. There is no second piece of code to keep in sync.

Here is the same result, `Author → Work → genres`, built both ways:

=== ":material-close-circle-outline: Hand-written Polars"

    ```python
    import polars as pl
    from pydantic import BaseModel


    class Work(BaseModel):
        title: str
        year: int
        genres: list[str]


    class Author(BaseModel):
        name: str
        born: int
        works: list[Work]


    records = (
        pl.LazyFrame(rows)
        .group_by("author", "title", maintain_order=True)
        .agg(
            pl.col("born").first(),
            pl.col("year").first(),
            pl.col("genre").drop_nulls().unique(maintain_order=True).alias("genres"),
        )
        .group_by("author", maintain_order=True)
        .agg(
            pl.col("born").first(),
            pl.struct("title", "year", "genres").alias("works"),
        )
        .rename({"author": "name"})
        .collect()
        .to_dicts()
    )
    authors = [Author.model_validate(record) for record in records]
    ```

    The models describe the shape, and **a separate pipeline repeats that shape by hand**.
    Add a field, rename a column or nest one level deeper, and both must change in step.

=== ":material-check-circle-outline: `graphty`"

    ```python
    from pydantic import BaseModel, Field
    from graphty import ConfigDict, ModelMaterializer


    class Work(BaseModel):
        model_config = ConfigDict(group_by="title")

        title: str
        year: int
        genres: list[str] = Field(validation_alias="genre")


    class Author(BaseModel):
        model_config = ConfigDict(group_by="name")

        name: str = Field(validation_alias="author")
        born: int
        works: list[Work]


    authors = ModelMaterializer(model=Author, data=rows).generate_models()
    ```

    **One source of truth.** `graphty` reads the models and compiles the Polars plan for you.

## At a glance

|                                   | Hand-written pipeline         | `graphty`                          |
|-----------------------------------|-------------------------------|----------------------------------|
| Source of truth for the shape     | Models **and** pipeline       | :material-check: Models only     |
| Adding a nested level             | Rewrite the group-by chain    | :material-check: Add a field     |
| Validation                        | Separate step                 | :material-check: Built in        |
| Execution engine                  | Polars, if you write it so    | :material-check: Polars, always  |
| Polymorphic rows (unions)         | Custom branching code         | :material-check: Pydantic unions |
| Learning curve for Pydantic users | Polars API on top             | :material-check: One config key  |

## Design principles

`graphty` is deliberately small:

- **Stay close to Pydantic.** `ConfigDict(group_by=...)` and `list` fields as aggregation targets
  are the core extensions. Everything else is standard Pydantic: validation, aliases, validators
  and serialization.
- **Do one thing well.** A solid core, with recipes and usage patterns preferred over features.
- **Simple and deep.** A small API surface hiding a capable, recursive planner.
