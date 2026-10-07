import logging
from collections.abc import Iterator

import polars as pl
from pydantic import BaseModel

from graphty.planner import LazyFramePlanner
from graphty.utils.structlog import StructuredMessage

logger = logging.getLogger(__name__)


class ModelMaterializer[TModel: BaseModel]:
    def __init__(
        self, model: type[TModel], data: pl._typing.FrameInitTypes | pl.LazyFrame
    ) -> None:
        self.model = model
        self.planner = LazyFramePlanner(model=model, data=data)

    def plan(self) -> pl.LazyFrame:
        return self.planner.run()

    def collect(self) -> pl.DataFrame:
        lazy_frame: pl.LazyFrame = self.plan()
        return lazy_frame.collect(engine="streaming")

    def generate_bindings(self) -> Iterator[dict[str, object]]:
        data_frame: pl.DataFrame = self.collect()
        return data_frame.iter_rows(named=True)

    def generate_models(self) -> Iterator[TModel]:
        for binding in self.generate_bindings():
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(
                    StructuredMessage(
                        message="Instantiating model.",
                        model=self.model,
                        binding=binding,
                    )
                )
            yield self.model.model_validate(binding)
