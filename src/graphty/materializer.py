import logging
from collections.abc import Iterator
from functools import cached_property

import polars as pl
from pydantic import BaseModel

from graphty.planner import LazyFramePlanner
from graphty.utils.structlog import StructuredMessage

logger = logging.getLogger(__name__)


class ModelMaterializer[TModel: BaseModel]:
    def __init__(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self._model = model
        self._planner = LazyFramePlanner(model=model, data=data)

    @cached_property
    def df(self) -> pl.DataFrame:
        lazy_frame: pl.LazyFrame = self._planner.run()
        return lazy_frame.collect()

    def generate_bindings(self) -> Iterator[dict[str, object]]:
        return self.df.iter_rows(named=True)

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
