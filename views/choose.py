from flask import Blueprint, render_template, request, redirect

from classes.units.enemy import Enemy
from classes.units.player import Player
from container import result_choice_hero, units, equipment, heroes, result_choice_enemy

choose_blueprint = Blueprint('choose_blueprint', __name__, template_folder='./templates')


@choose_blueprint.get("/choose-hero/")
def choose_player_get():
    """
    Вьюшка выбора персонажа для игрока
    """
    return render_template('hero_choosing.html', result=result_choice_hero)


@choose_blueprint.post("/choose-hero/")
def choose_player_post():
    """
    Вьюшка для обработки выбора игрока
    """
    name = request.form.get('name')
    unit = units.get_hero_by_class(request.form.get('unit_class'))
    weapon = equipment.get_weapon(request.form.get('weapon'))
    armor = equipment.get_armor(request.form.get('armor'))
    heroes['player'] = Player(name, unit, weapon, armor)
    return redirect('/choose-enemy/')


@choose_blueprint.get("/choose-enemy/")
def choose_enemy_get():
    """
    Вьюшка для выбора противника
    """
    return render_template('hero_choosing.html', result=result_choice_enemy)


@choose_blueprint.post("/choose-enemy/")
def choose_enemy_post():
    """
    Вьюшка для обработки выбора противника
    """
    name = request.form.get('name')
    unit = units.get_hero_by_class(request.form.get('unit_class'))
    weapon = equipment.get_weapon(request.form.get('weapon'))
    armor = equipment.get_armor(request.form.get('armor'))
    heroes['enemy'] = Enemy(name, unit, weapon, armor)
    return redirect('/fight/')
