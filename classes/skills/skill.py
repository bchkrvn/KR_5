from classes.skills.skill_base import SkillBase

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.units.unit_base import UnitBase


class Skill(SkillBase):
    def __init__(self, name: str, stamina: int, damage: int):
        self._name = name
        self._stamina = stamina
        self._damage = damage

    @property
    def name(self) -> str:
        return self._name

    @property
    def stamina(self) -> int:
        return self._stamina

    @property
    def damage(self) -> int:
        return self._damage

    def skill_effect(self, user: UnitBase, target: UnitBase):
        user.subtract_stamina(self.stamina)
        target.get_damage(self.damage)
        return f'{user.name} применил навык "{self.name}" против {target.name} и нанес {self.damage} урона! '

    def _is_stamina_enough(self, user):
        return user.stamina > self.stamina

    def use(self, user: UnitBase, target: UnitBase) -> str:
        if self._is_stamina_enough(user):
            return self.skill_effect(user, target)
        return f"{user.name} попытался использовать {self._name} но у него не хватило выносливости. "
