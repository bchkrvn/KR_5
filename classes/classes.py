import json
from dataclasses import dataclass

from classes.skills import Skill
from constants import UNIT_PATH


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


def get_units(skills: dict[str, Skill]) -> dict[str, UnitClass]:
    try:
        with open(UNIT_PATH) as file:
            units_data = json.load(file)
    except FileNotFoundError:
        return dict()

    for unit in units_data:
        unit['skill'] = skills[unit['skill']]

    units_dict = dict()
    for unit in units_data:
        unit_object = UnitClass(**unit)
        units_dict[unit_object.name] = unit_object

    return units_dict
