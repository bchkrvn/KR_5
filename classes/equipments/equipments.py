import json

from classes.equipments.armor import Armor
from classes.equipments.equipment_data import EquipmentData
from classes.equipments.weapon import Weapon
from constants import EQUIPMENT_PATH


class Equipments:
    """
    Класс хранения всех видов амуниции героев
    """

    def __init__(self):
        self._equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        """
        Получить оружие по его названию
        """
        return self._equipment.weapons[weapon_name]

    def get_armor(self, armor_name) -> Armor:
        """
        Получить брони по ее названию
        """
        return self._equipment.armors[armor_name]

    def get_weapons_names(self) -> list:
        """
        Получить список названий оружия
        """
        return list(self._equipment.weapons.keys())

    def get_armors_names(self) -> list:
        """
        Получить список названий брони
        """
        return list(self._equipment.armors.keys())

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        """
        Получить данные об амуниции из json файла
        """
        try:
            with open(EQUIPMENT_PATH) as file:
                equipment_data = json.load(file)
        except FileNotFoundError:
            equipment_data = dict()

        weapons = {weapon['name']: Weapon(**weapon) for weapon in equipment_data['weapons']}
        armors = {armor['name']: Armor(**armor) for armor in equipment_data['armors']}

        return EquipmentData(weapons, armors)

    def __repr__(self):
        return f'Equipment weapons:{self.get_weapons_names()}, armors:{self.get_armors_names()}'
