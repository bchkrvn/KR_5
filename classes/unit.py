from __future__ import annotations

import random
from abc import ABC

from classes.hero.heroes import Hero
from classes.equipments.equipments import Weapon, Armor


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """

    def __init__(self, name: str, unit_class: Hero, weapon: Weapon, armor: Armor):
        """
        При инициализации класса Unit используем свойства класса UnitClass
        """
        self.name = name
        self.unit_class = unit_class
        self.hp = unit_class.max_health
        self.stamina = unit_class.max_stamina
        self.weapon = weapon
        self.armor = armor
        self._is_skill_used = False

    @property
    def health_points(self) -> float:
        return self.hp

    @property
    def stamina_points(self) -> float:
        return self.stamina

    def equip_weapon(self, weapon: Weapon) -> str:
        self.weapon = weapon
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor) -> str:
        self.armor = armor
        return f"{self.name} экипирован броней {self.weapon.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        absolute_damage = round(self.weapon.damage * self.unit_class.attack, 1)
        self.subtract_stamina(self.weapon.stamina_per_hit)

        if target.armor.stamina_per_turn > target.stamina_points:
            protection = 0
        else:
            protection = round(target.armor.defence * target.unit_class.armor, 1)
            target.subtract_stamina(target.armor.stamina_per_turn)

        damage = round(absolute_damage - protection, 1)
        if damage > 0:
            target.get_damage(damage)
        return damage

    def get_damage(self, damage: float) -> None:
        if self.hp > damage:
            self.hp = round(self.hp - damage, 1)
        else:
            self.hp = 0

    def subtract_stamina(self, stamina: float) -> None:
        self.stamina = round(self.stamina - stamina, 1)

    def add_stamina(self, stamina: float) -> None:
        self.stamina = round(self.stamina + stamina * self.unit_class.stamina, 1)

        if self.stamina > self.unit_class.max_stamina:
            self.stamina = self.unit_class.max_stamina

    def hit(self, target: BaseUnit) -> str:

        if self.weapon.stamina_per_hit > self.stamina_points:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости. "

        damage = self._count_damage(target)

        if damage > 0:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона. "
        else:
            return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает. "

    def use_skill(self, target: BaseUnit) -> str:
        if self._is_skill_used:
            return f'Навык  {self.unit_class.skill.name} уже использован! '

        self._is_skill_used = True
        return self.unit_class.skill.use(self, target)


class PlayerUnit(BaseUnit):
    def __init__(self, name: str, unit_class: Hero, weapon: Weapon, armor: Armor):
        super().__init__(name, unit_class, weapon, armor)


class EnemyUnit(BaseUnit):
    def __init__(self, name: str, unit_class: Hero, weapon: Weapon, armor: Armor):
        super().__init__(name, unit_class, weapon, armor)

    def hit(self, target: BaseUnit) -> str:
        if not self._is_skill_used and self.stamina_points > self.unit_class.skill.stamina:
            random_number = random.randint(1, 10)

            if random_number == 1:
                return self.use_skill(target)

        return super().hit(target)
