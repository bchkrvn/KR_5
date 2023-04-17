from dataclasses import dataclass


@dataclass
class Armor:
    """
    Датакласс защиты
    """
    id: int
    name: str
    defence: float
    stamina_per_turn: float
