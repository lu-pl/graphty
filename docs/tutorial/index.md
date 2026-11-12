# Tutorial

`graphty` is a Python library for materializing [Pydantic](https://docs.pydantic.dev) object graphs from relational data.

The core idea of `graphty` is to utilize Pydantic models as a declarative DSL for building [Polars](https://pola.rs) query plans.

Instead of writing imperative data transformation code — group this, aggregate that, nest this inside that — users should be able to define the shape of what they want as a Pydantic model hierarchy; and `graphty` figures out the respective materialization from flat tabular data.

> `graphty` interprets Pydantic models as DataFrame transformation specifications.

More concretely, the library addresses the *structural* [impedance mismatch](https://en.wikipedia.org/wiki/Object%E2%80%93relational_impedance_mismatch) between flat relational data representations and hierarchical object models. It extends Pydantic with a small declarative DSL for expressing grouping, aggregation, and deduplication operations. These transformations are compiled into Polars expressions, yielding records that are subsequently validated and materialized as Pydantic model objects.

Although originally developed for implementing typed REST APIs over SPARQL endpoints, the model materializer can be applied to any tabular data representation, including SQL query results, CSV files, dataframes, etc.

This tutorial introduces the `graphty` DSL step by step and explains the rationale behind the library as well as how it works under the hood.


