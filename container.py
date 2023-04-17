from classes.classes import Units
from classes.equipments.equipments import Equipments
from classes.skills import Skills

skills = Skills()
units = Units(skills.get_skills())
equipment = Equipments()

result_choice_hero = {
    'header': 'Выберите героя',
    'classes': list(units.get_units().keys()),
    'weapons': equipment.get_weapons_names(),
    'armors': equipment.get_armors_names(),
}

result_choice_enemy = {
    'header': 'Выберите врага',
    'classes': list(units.get_units().keys()),
    'weapons': equipment.get_weapons_names(),
    'armors': equipment.get_armors_names(),
}
