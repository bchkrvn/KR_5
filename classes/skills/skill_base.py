from abc import abstractmethod, ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.unit import BaseUnit


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
    def skill_effect(self, user: BaseUnit, target: BaseUnit) -> str:
        pass

    @abstractmethod
    def _is_stamina_enough(self, user) -> bool:
        pass

    @abstractmethod
    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        pass

    def __repr__(self):
        return f"Skill {self.name}"
