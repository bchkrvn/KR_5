from random import random
from typing import TYPE_CHECKING
from classes.units.unit_base import UnitBase

if TYPE_CHECKING:
    from classes.equipments.armor import Armor
    from classes.equipments.weapon import Weapon
    from classes.hero.hero import Hero


class Enemy(UnitBase):
    def __init__(self, name: str, unit_class: Hero, weapon: Weapon, armor: Armor):
        super().__init__(name, unit_class, weapon, armor)

    def hit(self, target: UnitBase) -> str:
        if not self._is_skill_used and self.stamina_points > self.unit_class.skill.stamina:
            random_number = random.randint(1, 10)

            if random_number == 1:
                return self.use_skill(target)

        return super().hit(target)
