from __future__ import annotations
import json

from classes.skills.skill import Skill
from constants import SKILLS_PATH


class Skills:
    """
    Класс хранения всех навыков героев
    """
    def __init__(self):
        self._skills = self._get_skills_from_json()

    @staticmethod
    def _get_skills_from_json() -> dict[str:Skill]:
        """
        Загрузить список всех навыков из json
        """
        try:
            with open(SKILLS_PATH) as file:
                skills_data = json.load(file)
        except FileNotFoundError:
            return dict()

        skills_dict = {skill['name']: Skill(**skill) for skill in skills_data}
        return skills_dict

    def get_skills(self) -> dict[str:Skill]:
        """
        Получить словарь со всеми навыками
        """
        return self._skills

    def __repr__(self):
        return f'Skills {list(self._skills.keys())}'
