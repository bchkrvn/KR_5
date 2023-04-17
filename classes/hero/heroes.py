import json

from classes.hero.hero import Hero
from classes.skills.skill import Skill
from constants import HEROES_PATH


class Heroes:
    """
    Класс хранения всех видов героев для игры
    """

    def __init__(self, skills: dict[str, Skill]):
        self._heroes = self._get_heroes_from_json(skills)

    @staticmethod
    def _get_heroes_from_json(skills: dict[str, Skill]) -> dict[str, Hero]:
        """
        Получить всех героев из json файла
        """
        try:
            with open(HEROES_PATH) as file:
                heroes_data: dict = json.load(file)
        except FileNotFoundError:
            return dict()

        for hero in heroes_data:
            hero['skill'] = skills[hero['skill']]

        heroes_dict = {hero['name']: Hero(**hero) for hero in heroes_data}
        return heroes_dict

    def get_heroes(self) -> dict[str, Hero]:
        """
        Получить словарь со всеми видами героев для игры
        """
        return self._heroes

    def get_hero_by_class(self, unit_class: str) -> Hero:
        """
        Получить объект класса герой по его названию
        """
        return self._heroes[unit_class]

    def __repr__(self) -> str:
        return f'Skills {list(self._heroes.keys())}'
