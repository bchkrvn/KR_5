from __future__ import annotations
from abc import ABC, abstractmethod

from classes.classes import UnitClass
from classes.equipment import Weapon, Armor
from typing import Optional


class BaseUnit(ABC):
    """
    Базовый класс юнита
    """

    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
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
    def health_points(self):
        return self.hp

    @property
    def stamina_points(self):
        return self.stamina

    def equip_weapon(self, weapon: Weapon):
        # TODO присваиваем нашему герою новое оружие
        return f"{self.name} экипирован оружием {self.weapon.name}"

    def equip_armor(self, armor: Armor):
        # TODO одеваем новую броню
        return f"{self.name} экипирован броней {self.weapon.name}"

    def _count_damage(self, target: BaseUnit) -> int:
        # TODO Эта функция должна содержать:
        #  логику расчета урона игрока
        #  логику расчета брони цели
        #  здесь же происходит уменьшение выносливости атакующего при ударе
        #  и уменьшение выносливости защищающегося при использовании брони
        #  если у защищающегося нехватает выносливости - его броня игнорируется
        #  после всех расчетов цель получает урон - target.get_damage(damage)
        #  и возвращаем предполагаемый урон для последующего вывода пользователю в текстовом виде
        absolute_damage = round(self.weapon.damage() * self.unit_class.attack, 1)
        self.subtract_stamina(self.weapon.stamina_per_hit)

        if target.armor.stamina_per_turn > target.stamina_points:
            protection = 0
        else:
            protection = round(target.armor.defence * target.unit_class.armor, 1)
            target.subtract_stamina(target.armor.stamina_per_turn)

        damage = absolute_damage - protection
        if damage > 0:
            target.get_damage(damage)
        return damage

    def get_damage(self, damage: float):
        if self.hp > damage:
            self.hp -= damage
        else:
            self.hp = 0

    def subtract_stamina(self, stamina: float):
        self.stamina -= stamina

    def add_stamina(self, stamina: float):
        self.stamina += stamina * self.unit_class.stamina
        if self.stamina > self.unit_class.max_stamina:
            self.stamina = self.unit_class.max_stamina

    @abstractmethod
    def hit(self, target: BaseUnit) -> str:
        """
        этот метод будет переопределен ниже
        """
        pass

    def use_skill(self, target: BaseUnit) -> str:
        """
        метод использования умения.
        если умение уже использовано возвращаем строку
        Навык использован
        Если же умение не использовано тогда выполняем функцию
        self.unit_class.skill.use(user=self, target=target)
        и уже эта функция вернем нам строку которая характеризует выполнение умения
        """
        if self._is_skill_used:
            return f'Навык  {self.unit_class.skill.name} уже использован'
        pass


class PlayerUnit(BaseUnit):
    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        super().__init__(name, unit_class, weapon, armor)

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар игрока:
        здесь происходит проверка достаточно ли выносливости для нанесения удара.
        вызывается функция self._count_damage(target)
        а также возвращается результат в виде строки
        """
        if self.weapon.stamina_per_hit > self.stamina_points:
            return f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."

        damage = self._count_damage(target)

        if damage > 0:
            return f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} соперника и наносит {damage} урона."
        else:
            return f"{self.name} используя {self.weapon.name} наносит удар, но {target.armor.name} cоперника его останавливает."



class EnemyUnit(BaseUnit):
    def __init__(self, name: str, unit_class: UnitClass, weapon: Weapon, armor: Armor):
        super().__init__(name, unit_class, weapon, armor)

    def hit(self, target: BaseUnit) -> str:
        """
        функция удар соперника
        должна содержать логику применения соперником умения
        (он должен делать это автоматически и только 1 раз за бой).
        Например, для этих целей можно использовать функцию randint из библиотеки random.
        Если умение не применено, противник наносит простой удар, где также используется
        функция _count_damage(target
        """
        # TODO результат функции должен возвращать результат функции skill.use или же следующие строки:
        f"{self.name} используя {self.weapon.name} пробивает {target.armor.name} и наносит Вам {damage} урона."
        f"{self.name} используя {self.weapon.name} наносит удар, но Ваш(а) {target.armor.name} его останавливает."
        f"{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости."


