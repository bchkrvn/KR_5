import random
from dataclasses import dataclass


@dataclass
class Weapon:
    """
    Датакласс оружия
    """
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        """
        Функция для получения рандомного урона в заданном диапазоне
        """
        return round(random.uniform(self.min_damage, self.max_damage), 1)
