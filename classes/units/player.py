from typing import TYPE_CHECKING

from classes.units.unit_base import UnitBase

if TYPE_CHECKING:
    from classes.equipments.armor import Armor
    from classes.equipments.weapon import Weapon
    from classes.hero.hero import Hero


class Player(UnitBase):
    def __init__(self, name: str, unit_class: Hero, weapon: Weapon, armor: Armor):
        super().__init__(name, unit_class, weapon, armor)
