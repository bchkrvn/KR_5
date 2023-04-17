class Skill:
    """
    Класс навыков героев
    """

    def __init__(self, name: str, stamina: float, damage: float):
        self._name = name
        self._stamina = stamina
        self._damage = damage

    @property
    def name(self) -> str:
        return self._name

    @property
    def stamina(self) -> float:
        return self._stamina

    @property
    def damage(self) -> float:
        return self._damage

    def _skill_effect(self, user, target) -> str:
        """
        Функция для применения навыка героя
        """
        user.subtract_stamina(self.stamina)
        target.get_damage(self.damage)
        return f'{user.name} применил навык "{self.name}" против {target.name} и нанес {self.damage} урона! '

    def _is_stamina_enough(self, user) -> bool:
        """
        Проверка достаточно ли выносливости для навыка
        """
        return user.stamina > self.stamina

    def use(self, user, target) -> str:
        """
        Функция для проверки и выполнения навыка героя
        """
        if self._is_stamina_enough(user):
            return self._skill_effect(user, target)
        return f"{user.name} попытался использовать {self._name} но у него не хватило выносливости. "

    def __repr__(self):
        return f"Skill {self.name}"
