from dataclasses import dataclass
from random import random


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(random.uniform(self.min_damage, self.max_damage), 1)

