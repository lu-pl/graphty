"""Tests for the Author/Work reference case."""

from dataclasses import dataclass

import pytest
from graphty import ConfigDict, ModelMaterializer
from inline_snapshot import snapshot
from pydantic import BaseModel


class Work(BaseModel):
    model_config = ConfigDict(group_by="work_name")

    work_name: str
    viaf: list[str]


class Author(BaseModel):
    model_config = ConfigDict(group_by="name")

    gnd: str
    name: str
    works: list[Work | None]
    educated_at: list[str]


data = [
    {
        "work": "http://www.wikidata.org/entity/Q1497409",
        "gnd": "119359464",
        "work_name": "Gebürtig",
        "name": "Schindel",
        "viaf": "123",
        "educated_at": None,
    },
    {
        "work": "http://www.wikidata.org/entity/Q15805238",
        "gnd": "115612815",
        "work_name": "Der alte König in seinem Exil",
        "name": "Geiger",
        "viaf": "299260555",
        "educated_at": "University of Vienna",
    },
    {
        "work": "http://www.wikidata.org/entity/Q15805238",
        "gnd": "115612815",
        "work_name": "Der alte König in seinem Exil",
        "name": "Geiger",
        "viaf": "6762154387354230970008",
        "educated_at": "University of Vienna",
    },
    {
        "work": "http://www.wikidata.org/entity/Q58038819",
        "gnd": "115612815",
        "work_name": "Unter der Drachenwand",
        "name": "Geiger",
        "viaf": "2277151717053313900002",
        "educated_at": "University of Vienna",
    },
    {
        "work": "http://www.wikidata.org/entity/Q100266054",
        "gnd": "1136992030",
        "work_name": "Das flüssige Land",
        "name": "Edelbauer",
        "viaf": "456",
        "educated_at": "University of Vienna",
    },
    {
        "work": "http://www.wikidata.org/entity/Q100266054",
        "gnd": "1136992030",
        "work_name": "Das flüssige Land",
        "name": "Edelbauer",
        "viaf": "789",
        "educated_at": "University of Applied Arts Vienna",
    },
]


@dataclass
class Parameter:
    model: object
    data: object
    bindings: object
    model_dump: object


params: list[Parameter] = [
    Parameter(
        model=Author,
        data=data,
        bindings=snapshot(
            [
                {
                    "name": "Schindel",
                    "gnd": "119359464",
                    "works": [{"work_name": "Gebürtig", "viaf": ["123"]}],
                    "educated_at": [],
                },
                {
                    "name": "Geiger",
                    "gnd": "115612815",
                    "works": [
                        {
                            "work_name": "Der alte König in seinem Exil",
                            "viaf": ["299260555", "6762154387354230970008"],
                        },
                        {
                            "work_name": "Unter der Drachenwand",
                            "viaf": ["2277151717053313900002"],
                        },
                    ],
                    "educated_at": ["University of Vienna"],
                },
                {
                    "name": "Edelbauer",
                    "gnd": "1136992030",
                    "works": [
                        {"work_name": "Das flüssige Land", "viaf": ["456", "789"]}
                    ],
                    "educated_at": [
                        "University of Vienna",
                        "University of Applied Arts Vienna",
                    ],
                },
            ]
        ),
        model_dump=snapshot(
            [
                {
                    "gnd": "119359464",
                    "name": "Schindel",
                    "works": [{"work_name": "Gebürtig", "viaf": ["123"]}],
                    "educated_at": [],
                },
                {
                    "gnd": "115612815",
                    "name": "Geiger",
                    "works": [
                        {
                            "work_name": "Der alte König in seinem Exil",
                            "viaf": ["299260555", "6762154387354230970008"],
                        },
                        {
                            "work_name": "Unter der Drachenwand",
                            "viaf": ["2277151717053313900002"],
                        },
                    ],
                    "educated_at": ["University of Vienna"],
                },
                {
                    "gnd": "1136992030",
                    "name": "Edelbauer",
                    "works": [
                        {"work_name": "Das flüssige Land", "viaf": ["456", "789"]}
                    ],
                    "educated_at": [
                        "University of Vienna",
                        "University of Applied Arts Vienna",
                    ],
                },
            ]
        ),
    ),
]


@pytest.mark.parametrize("param", params)
def test_materalizer_author_work(param):

    materializer = ModelMaterializer(model=param.model, data=param.data)

    bindings = list(materializer.generate_bindings())
    model_dump = [model.model_dump() for model in materializer.generate_models()]

    assert bindings == param.bindings
    assert model_dump == param.model_dump
