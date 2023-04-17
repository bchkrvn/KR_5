from flask import Flask, render_template, request, redirect

from classes.units.enemy import Enemy
from classes.units.player import Player
from container import result_choice_hero, units, result_choice_enemy, equipment, arena, heroes

app = Flask(__name__)


@app.route("/")
def menu_page():
    return render_template('index.html')


@app.route("/fight/")
def start_fight():
    arena.start_game(**heroes)
    return render_template('fight.html', heroes=heroes)


@app.route("/fight/hit")
def hit():
    if arena.game_is_running:
        player_result = arena.player_hit()
        enemy_result = arena.enemy_hit()
        battle_result = arena.battle_result()

        if battle_result:
            arena.end_game()
        return render_template('fight.html',
                               heroes=heroes,
                               result=player_result + enemy_result,
                               battle_result=battle_result)

    else:
        battle_result = arena.battle_result()
        return render_template('fight.html',
                               heroes=heroes,
                               battle_result=battle_result)


@app.route("/fight/use-skill")
def use_skill():
    if arena.game_is_running:
        player_result = arena.player_use_skill()
        enemy_result = arena.enemy_hit()
        battle_result = arena.battle_result()
        if battle_result:
            arena.end_game()
        return render_template('fight.html',
                               heroes=heroes,
                               result=player_result + enemy_result,
                               battle_result=battle_result)

    else:
        battle_result = arena.battle_result()
        return render_template('fight.html',
                               heroes=heroes,
                               battle_result=battle_result)


@app.route("/fight/pass-turn")
def pass_turn():
    if arena.game_is_running:
        player_result = arena.player_pass()
        enemy_result = arena.enemy_hit()
        battle_result = arena.battle_result()
        if battle_result:
            arena.end_game()
        return render_template('fight.html',
                               heroes=heroes,
                               result=player_result + enemy_result,
                               battle_result=battle_result)

    else:
        battle_result = arena.battle_result()
        return render_template('fight.html',
                               heroes=heroes,
                               battle_result=battle_result)


@app.route("/fight/end-fight")
def end_fight():
    arena.end_game()
    return render_template("index.html")


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    if request.method == 'GET':
        return render_template('hero_choosing.html', result=result_choice_hero)

    elif request.method == 'POST':
        name = request.form.get('name')
        unit = units.get_hero_by_class(request.form.get('unit_class'))
        weapon = equipment.get_weapon(request.form.get('weapon'))
        armor = equipment.get_armor(request.form.get('armor'))
        heroes['player'] = Player(name, unit, weapon, armor)
        return redirect('/choose-enemy/')


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    if request.method == 'GET':
        return render_template('hero_choosing.html', result=result_choice_enemy)

    elif request.method == 'POST':
        name = request.form.get('name')
        unit = units.get_hero_by_class(request.form.get('unit_class'))
        weapon = equipment.get_weapon(request.form.get('weapon'))
        armor = equipment.get_armor(request.form.get('armor'))
        heroes['enemy'] = Enemy(name, unit, weapon, armor)
        return redirect('/fight/')


if __name__ == "__main__":
    app.run(debug=True)
