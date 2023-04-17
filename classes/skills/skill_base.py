from abc import abstractmethod, ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from classes.units.unit_base import UnitBase


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
    def skill_effect(self, user: UnitBase, target: UnitBase) -> str:
        pass

    @abstractmethod
    def _is_stamina_enough(self, user) -> bool:
        pass

    @abstractmethod
    def use(self, user: UnitBase, target: UnitBase) -> str:
        pass

    def __repr__(self):
        return f"Skill {self.name}"
