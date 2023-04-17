import random
from classes.units.unit_base import UnitBase

from classes.equipments.armor import Armor
from classes.equipments.weapon import Weapon
from classes.hero.hero import Hero


class Enemy(UnitBase):
    """
    Класс соперника
    """
    def __init__(self, name: str, unit_class: Hero, weapon: Weapon, armor: Armor):
        super().__init__(name, unit_class, weapon, armor)

    def hit(self, target: UnitBase) -> str:
        """
        Функция выбора действия противника
        Противник может:
        1) воспользоваться навыком с вероятностью 10%
        2) пропустить ход с вероятностью 10%
        3) воспользоваться обычным ударом в остальных случаях
        """
        random_number = random.randint(1, 10)

        # Если навык не использован, выносливости достаточно и выпало нужное число
        if not self._is_skill_used and self.stamina_points > self.unit_class.skill.stamina and random_number == 1:
            return self.use_skill(target)

        if random_number == 2:
            return f'{self.name} пропустил ход. '

        return super().hit(target)
