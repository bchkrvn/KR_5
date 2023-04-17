from __future__ import annotations
import json

from classes.skills.skill import Skill
from constants import SKILL_PATH


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
