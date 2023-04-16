from __future__ import annotations

import json
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

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

    def skill_effect(self):
        # TODO логика использования скилла -> return str
        # TODO в классе нам доступны экземпляры user и target - можно использовать любые их методы
        # TODO именно здесь происходит уменшение стамины у игрока применяющего умение и
        # TODO уменьшение здоровья цели.
        # TODO результат применения возвращаем строкой
        pass

    def _is_stamina_enough(self, user):
        return user.stamina > self.stamina

    def use(self, user: BaseUnit) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        if self._is_stamina_enough(user):
            return self.skill_effect()
        return f"{user.name} попытался использовать {self._name} но у него не хватило выносливости."

    def __repr__(self):
        return f"Skill {self.name}"


def skills() -> dict[str:Skill]:
    try:
        with open('../data/skills.json') as file:
            skills_data = json.load(file)
    except FileNotFoundError:
        return dict()

    skills_dict = dict()
    for skill in skills_data:
        skill_object = Skill(**skill)
        skills_dict[skill_object.name] = skill_object

    return skills_dict
