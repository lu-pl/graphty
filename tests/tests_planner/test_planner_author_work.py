"""Tests for the Author/Work reference case."""

from graphty.planner import ConfigDict, LazyFramePlanner
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


EXPECTED = [
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
            {"work_name": "Unter der Drachenwand", "viaf": ["2277151717053313900002"]},
        ],
        "educated_at": ["University of Vienna"],
    },
    {
        "name": "Edelbauer",
        "gnd": "1136992030",
        "works": [{"work_name": "Das flüssige Land", "viaf": ["456", "789"]}],
        "educated_at": ["University of Vienna", "University of Applied Arts Vienna"],
    },
]


def test_planner_author_work():
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

    planner = LazyFramePlanner(model=Author, data=data)
    frame = planner.run()

    assert frame.collect().to_dicts() == EXPECTED
