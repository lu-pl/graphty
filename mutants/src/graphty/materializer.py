import logging
from collections.abc import Iterator
from functools import cached_property

import polars as pl
from pydantic import BaseModel

from graphty.planner import LazyFramePlanner
from graphty.utils.structlog import StructuredMessage

logger = logging.getLogger(__name__)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁModelMaterializerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁModelMaterializerǁgenerate_bindings__mutmut: MutantDict = {}  # type: ignore
mutants_xǁModelMaterializerǁgenerate_models__mutmut: MutantDict = {}  # type: ignore


class ModelMaterializer[TModel: BaseModel]:
    @_mutmut_mutated(mutants_xǁModelMaterializerǁ__init____mutmut)
    def __init__(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = model
        self._planner = LazyFramePlanner(model=model, data=data)
    def xǁModelMaterializerǁ__init____mutmut_orig(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = model
        self._planner = LazyFramePlanner(model=model, data=data)
    def xǁModelMaterializerǁ__init____mutmut_1(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = None
        self._planner = LazyFramePlanner(model=model, data=data)
    def xǁModelMaterializerǁ__init____mutmut_2(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = model
        self._planner = None
    def xǁModelMaterializerǁ__init____mutmut_3(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = model
        self._planner = LazyFramePlanner(model=None, data=data)
    def xǁModelMaterializerǁ__init____mutmut_4(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = model
        self._planner = LazyFramePlanner(model=model, data=None)
    def xǁModelMaterializerǁ__init____mutmut_5(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = model
        self._planner = LazyFramePlanner(data=data)
    def xǁModelMaterializerǁ__init____mutmut_6(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = model
        self._planner = LazyFramePlanner(model=model, )

    @cached_property
    def df(self) -> pl.DataFrame:
        lazy_frame: pl.LazyFrame = self._planner.run()
        return lazy_frame.collect(engine="streaming")

    @_mutmut_mutated(mutants_xǁModelMaterializerǁgenerate_bindings__mutmut)
    def generate_bindings(self) -> Iterator[dict[str, object]]:
        return self.df.iter_rows(named=True)

    def xǁModelMaterializerǁgenerate_bindings__mutmut_orig(self) -> Iterator[dict[str, object]]:
        return self.df.iter_rows(named=True)

    def xǁModelMaterializerǁgenerate_bindings__mutmut_1(self) -> Iterator[dict[str, object]]:
        return self.df.iter_rows(named=None)

    def xǁModelMaterializerǁgenerate_bindings__mutmut_2(self) -> Iterator[dict[str, object]]:
        return self.df.iter_rows(named=False)

    @_mutmut_mutated(mutants_xǁModelMaterializerǁgenerate_models__mutmut)
    def generate_models(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="Instantiating model.",
                    model=self._model,
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_orig(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="Instantiating model.",
                    model=self._model,
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_1(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                None
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_2(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message=None,
                    model=self._model,
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_3(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="Instantiating model.",
                    model=None,
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_4(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="Instantiating model.",
                    model=self._model,
                    binding=None,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_5(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    model=self._model,
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_6(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="Instantiating model.",
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_7(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="Instantiating model.",
                    model=self._model,
                    )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_8(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="XXInstantiating model.XX",
                    model=self._model,
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_9(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="instantiating model.",
                    model=self._model,
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_10(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="INSTANTIATING MODEL.",
                    model=self._model,
                    binding=binding,
                )
            )
            yield self._model.model_validate(binding)

    def xǁModelMaterializerǁgenerate_models__mutmut_11(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            logger.debug(
                StructuredMessage(
                    message="Instantiating model.",
                    model=self._model,
                    binding=binding,
                )
            )
            yield self._model.model_validate(None)

mutants_xǁModelMaterializerǁ__init____mutmut['_mutmut_orig'] = ModelMaterializer.xǁModelMaterializerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁ__init____mutmut['xǁModelMaterializerǁ__init____mutmut_1'] = ModelMaterializer.xǁModelMaterializerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁ__init____mutmut['xǁModelMaterializerǁ__init____mutmut_2'] = ModelMaterializer.xǁModelMaterializerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁ__init____mutmut['xǁModelMaterializerǁ__init____mutmut_3'] = ModelMaterializer.xǁModelMaterializerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁ__init____mutmut['xǁModelMaterializerǁ__init____mutmut_4'] = ModelMaterializer.xǁModelMaterializerǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁ__init____mutmut['xǁModelMaterializerǁ__init____mutmut_5'] = ModelMaterializer.xǁModelMaterializerǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁ__init____mutmut['xǁModelMaterializerǁ__init____mutmut_6'] = ModelMaterializer.xǁModelMaterializerǁ__init____mutmut_6 # type: ignore # mutmut generated

mutants_xǁModelMaterializerǁgenerate_bindings__mutmut['_mutmut_orig'] = ModelMaterializer.xǁModelMaterializerǁgenerate_bindings__mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_bindings__mutmut['xǁModelMaterializerǁgenerate_bindings__mutmut_1'] = ModelMaterializer.xǁModelMaterializerǁgenerate_bindings__mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_bindings__mutmut['xǁModelMaterializerǁgenerate_bindings__mutmut_2'] = ModelMaterializer.xǁModelMaterializerǁgenerate_bindings__mutmut_2 # type: ignore # mutmut generated

mutants_xǁModelMaterializerǁgenerate_models__mutmut['_mutmut_orig'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_orig # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_1'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_1 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_2'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_2 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_3'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_3 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_4'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_4 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_5'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_5 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_6'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_6 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_7'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_7 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_8'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_8 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_9'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_9 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_10'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_10 # type: ignore # mutmut generated
mutants_xǁModelMaterializerǁgenerate_models__mutmut['xǁModelMaterializerǁgenerate_models__mutmut_11'] = ModelMaterializer.xǁModelMaterializerǁgenerate_models__mutmut_11 # type: ignore # mutmut generated
