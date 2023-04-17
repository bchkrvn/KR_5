from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from constants import SKILL_PATH

if TYPE_CHECKING:
    from unit import BaseUnit


class SkillBase(ABC):
    """
    Базовый класс умения
    """

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def stamina(self) -> int:
        pass

    @property
    @abstractmethod
    def damage(self) -> int:
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    @abstractmethod
    def _is_stamina_enough(self, user) -> bool:
        pass

    @abstractmethod
    def use(self, user: BaseUnit) -> str:
        pass


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

    def skill_effect(self, user: BaseUnit, target: BaseUnit):
        user.subtract_stamina(self.stamina)
        target.get_damage(self.damage)
        return f'{user.name} применил навык "{self.name}" против {target.name} и нанес {self.damage} урона! '

    def _is_stamina_enough(self, user):
        return user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        if self._is_stamina_enough(user):
            return self.skill_effect(user, target)
        return f"{user.name} попытался использовать {self._name} но у него не хватило выносливости. "

    def __repr__(self):
        return f"Skill {self.name}"


class Skills:
    def __init__(self):
        self._skills = self._get_skills_from_json()

    @staticmethod
    def _get_skills_from_json() -> dict[str:Skill]:
        try:
            with open(SKILL_PATH) as file:
                skills_data = json.load(file)
        except FileNotFoundError:
            return dict()

        skills_dict = {skill['name']: Skill(**skill) for skill in skills_data}
        return skills_dict

    def get_skills(self):
        return self._skills

    def __repr__(self):
        return f'Skills {list(self._skills.keys())}'
