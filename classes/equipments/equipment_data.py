from dataclasses import dataclass

from classes.equipments.armor import Armor
from classes.equipments.weapon import Weapon


@dataclass
class EquipmentData:
    """
    Датакласс амуниции героев
    """
    weapons: dict[str, Weapon]
    armors: dict[str, Armor]
