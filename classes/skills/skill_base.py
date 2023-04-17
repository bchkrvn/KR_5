from abc import abstractmethod, ABC


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
    def skill_effect(self, user, target) -> str:
        pass

    @abstractmethod
    def _is_stamina_enough(self, user) -> bool:
        pass

    @abstractmethod
    def use(self, user, target) -> str:
        pass

    def __repr__(self):
        return f"Skill {self.name}"
