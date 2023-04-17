import json

from classes.equipments.armor import Armor
from classes.equipments.equipment_data import EquipmentData
from classes.equipments.weapon import Weapon
from constants import EQUIPMENT_PATH


class Equipments:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        return self.equipment.weapons[weapon_name]

    def get_armor(self, armor_name) -> Armor:
        return self.equipment.armors[armor_name]

    def get_weapons_names(self) -> list:
        return list(self.equipment.weapons.keys())

    def get_armors_names(self) -> list:
        return list(self.equipment.armors.keys())

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
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
