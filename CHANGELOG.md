# Changelog

## [0.7.0](https://github.com/lu-pl/graphty/compare/v0.6.0...v0.7.0) (2026-09-18)


### ⚠ BREAKING CHANGES

* implement extensible aggregation protocol

### Features

* implement extensible aggregation protocol ([1bd8fed](https://github.com/lu-pl/graphty/commit/1bd8fed0eef739d510ea9405bee6b11549477811))

## 0.1.0 (2026-09-17)


### ⚠ BREAKING CHANGES

* use custom AliasResolutionError
* raise NotImplementedError for unsupported aliasing options

### Features

* add ModelInfo and ModelInfoRegistry classes ([e6da474](https://github.com/lu-pl/graphty/commit/e6da47494812d74c8b3c61c7bc29e4295081ac2d))
* add StructuredMessage log message class ([75439b4](https://github.com/lu-pl/graphty/commit/75439b4815bdb19eaa8a4bd0f173f44a00596d73))
* check grouping key against model projection ([d79c5c7](https://github.com/lu-pl/graphty/commit/d79c5c7c9e5d0935d0d0cbf714545b1b36f586fa))
* defer schema collection in LazyFramePlanner ([7a8ff99](https://github.com/lu-pl/graphty/commit/7a8ff994efcae84e726343b2867cbc53a96aa02e))
* expose ConfigDict and Agg as public graphty symbols ([3ad5d2b](https://github.com/lu-pl/graphty/commit/3ad5d2b3fdf0f8293c9f267a499ef8c69851e2d5))
* expose ModelMaterializer as library-public symbol ([1b82388](https://github.com/lu-pl/graphty/commit/1b82388831a48aff71e124ff45e96c2c4ac4abc9))
* implement alias feature ([c4e7f40](https://github.com/lu-pl/graphty/commit/c4e7f408aaf8566d06480e83a7aa5b1655320073))
* implement AliasMap utility ([2397e1a](https://github.com/lu-pl/graphty/commit/2397e1a85e56ac0f927898ef02ca03f386019014))
* implement model-based column projection ([d9a3d8c](https://github.com/lu-pl/graphty/commit/d9a3d8cddb503b6c71e6bcfb603f6eeb41c715b2))
* implement model-based projection for ModelUnionDispatch ([e38660e](https://github.com/lu-pl/graphty/commit/e38660eec7dc260189744c71565eea0cda19ac0a))
* implement ModelMaterializer ([360d2ca](https://github.com/lu-pl/graphty/commit/360d2ca2744ada4789cc30aec850b5b9912e146d))
* implement nested tagged union resolution ([bc44f8d](https://github.com/lu-pl/graphty/commit/bc44f8d4c019162acc26ffdd80f8d2a4a434fe7f))
* introduce customs exceptions ([bd0994a](https://github.com/lu-pl/graphty/commit/bd0994a3d4f81e7addb738cb40dea7a27f573c58))
* make projection argument in AliasMap optional ([475146c](https://github.com/lu-pl/graphty/commit/475146ca8869d1c890996a3227138198c1ff4cff))
* raise NotImplementedError for unsupported aliasing options ([9de8ba4](https://github.com/lu-pl/graphty/commit/9de8ba45c9fab494d9daf8e979d22d68c9be3277))
* unify parametrized list code path in Exprs ([8464d3c](https://github.com/lu-pl/graphty/commit/8464d3c4cf4429d6b66f27bb9ffb1dfe9c4e3e87))
* use custom AliasResolutionError ([493aa54](https://github.com/lu-pl/graphty/commit/493aa54a0d4e2c426621e7e1667b4397cb9c25ce))
* use Polars streaming engine for dataframe collection ([8766041](https://github.com/lu-pl/graphty/commit/8766041916ac235d3c9fcab4145ce6aa5371a94f))


### Bug Fixes

* add guard for empty self.model_members ([c743fa1](https://github.com/lu-pl/graphty/commit/c743fa183f40d4f5c625fbf7a27caca1ac30f862))
* add model union check to is_pydantic_model_union_static_type ([b4b68a0](https://github.com/lu-pl/graphty/commit/b4b68a0c114951c7689192e268e8659cd05e296a))
* correct exclude values in toplevel base cols computation ([0af0155](https://github.com/lu-pl/graphty/commit/0af01553b57980882bc976862fe53a2785b07675))
* drop top-level grouping key if not in model_projection ([6bd5901](https://github.com/lu-pl/graphty/commit/6bd5901c53d3d9cfd6366e6ea87cc227102253b1))
* filter base cols for grouped models in LazyFramePlanner ([91c783e](https://github.com/lu-pl/graphty/commit/91c783e8bbd3c9b613b8d005c61ec5ab5e042324))
* filter toplevel base cols correctly ([7571940](https://github.com/lu-pl/graphty/commit/75719404d49c14b1cf6399b1ee20b5a02cc6d44b))
* handle aggregated union models correctly in Exprs ([5c3d6f4](https://github.com/lu-pl/graphty/commit/5c3d6f468eddb47ad8d10e9fdc9d960f351f31a6))
* handle empty models correctly ([d1731c6](https://github.com/lu-pl/graphty/commit/d1731c6027d61aa044bfd0b97cbdd129ccc543d0))
* pattern match single model union case ([d50ad25](https://github.com/lu-pl/graphty/commit/d50ad255ff5a34d865c7bdb54749bf80b1889416))
* skip union type forms in callable discriminator tag mapping ([56888ae](https://github.com/lu-pl/graphty/commit/56888aebda7ff43e2fe2ba5b9e0f25f1e4aeb83b))


### Documentation

* add basic installation info ([015065e](https://github.com/lu-pl/graphty/commit/015065e0f7b9cb75e8e6c6d75712cd6aa5c3d837))
* add comment to ModelUnionDispatch calls in LazyFramePlanner ([f58ea20](https://github.com/lu-pl/graphty/commit/f58ea201b982554da99d6008369db7fb6ad26a30))
* add intro to README ([5cf1f3c](https://github.com/lu-pl/graphty/commit/5cf1f3c4f589fc677389eeac631c3c3a2c05d8b3))
* add PyPI link ([34ab4d0](https://github.com/lu-pl/graphty/commit/34ab4d0e8acf710147d2d46b05a5bc09429b2d76))
* add ruff and uv badges ([6acfff2](https://github.com/lu-pl/graphty/commit/6acfff2359beb97c21de91596d130e4f88a8110b))
* add tests and coverage badge ([912d8a0](https://github.com/lu-pl/graphty/commit/912d8a06377a4f829ed94ae57779e5d069d87321))
* **readme:** add info about models as DataFrame operation specs ([2b5ab10](https://github.com/lu-pl/graphty/commit/2b5ab1034c3a9e24cc3058075abd52c062330818))
* **readme:** add section about graphty's core idea to the readme ([ab2e850](https://github.com/lu-pl/graphty/commit/ab2e850ece60d7e9d92f1212e6f5a8e5aab550e5))
* simplify README ([edbd3c9](https://github.com/lu-pl/graphty/commit/edbd3c978be0670eb1e01b98f38c2f755b928831))
* update readme ([f4c4f42](https://github.com/lu-pl/graphty/commit/f4c4f429b0f9ee56116bdf91e87db151d9c366ef))
