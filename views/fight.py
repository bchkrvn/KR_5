from flask import Blueprint, render_template, redirect

from container import heroes, arena

fight_blueprint = Blueprint('fight_blueprint', __name__, template_folder='./templates')


@fight_blueprint.get("/")
def start_fight():
    """
    Вьюшка для начала боя
    """
    arena.start_game(**heroes)
    return render_template('fight.html', heroes=heroes)


@fight_blueprint.get("/hit")
def hit():
    """
    Вьюшка для кнопки нанесения удара
    Осуществляет нанесение удара игроком и последующий удара соперником
    """
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


@fight_blueprint.get("/use-skill")
def use_skill():
    """
    Вьюшка для кнопки использовать навык
    Осуществляет использование навыка игроком и последующий удара соперником
    """
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


@fight_blueprint.get("/pass-turn")
def pass_turn():
    """
    Вьюшка для кнопки пропустить ход
    Осуществляет пропуск хода игроком и последующий удара соперником
    """
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


@fight_blueprint.get("/end-fight")
def end_fight():
    """
    Вьюшка кнопки закончить игру
    Завершает игру и перенаправляет на вьюшку меню
    """
    arena.end_game()
    return redirect("/")
