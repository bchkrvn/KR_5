from copy import copy

from flask import Flask, render_template, request, redirect

from classes.base import Arena
from classes.unit import PlayerUnit, EnemyUnit
from container import result_choice_hero, units, result_choice_enemy

app = Flask(__name__)

heroes = {
    "player": None,
    "enemy": None
}

arena = Arena()


@app.route("/")
def menu_page():
    # TODO рендерим главное меню (шаблон index.html)
    return render_template('index.html')


@app.route("/fight/")
def start_fight():

    pass

@app.route("/fight/hit")
def hit():
    # TODO кнопка нанесения удара
    # TODO обновляем экран боя (нанесение удара) (шаблон fight.html)
    # TODO если игра идет - вызываем метод player.hit() экземпляра класса арены
    # TODO если игра не идет - пропускаем срабатывание метода (простот рендерим шаблон с текущими данными)
    pass


@app.route("/fight/use-skill")
def use_skill():
    # TODO кнопка использования скилла
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    pass


@app.route("/fight/pass-turn")
def pass_turn():
    # TODO кнопка пропус хода
    # TODO логика пркатикчески идентична предыдущему эндпоинту
    # TODO однако вызываем здесь функцию следующий ход (arena.next_turn())
    pass


@app.route("/fight/end-fight")
def end_fight():
    # TODO кнопка завершить игру - переход в главное меню
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    # TODO кнопка выбор героя. 2 метода GET и POST
    # TODO на GET отрисовываем форму.
    # TODO на POST отправляем форму и делаем редирект на эндпоинт choose enemy
    if request.method == 'GET':
        return render_template('hero_choosing.html', result=result_choice_hero)
    elif request.method == 'POST':
        name = request.form.get('name')
        unit_class = request.form.get('unit_class')
        weapon = request.form.get('weapon')
        armor = request.form.get('armor')
        unit = units.get_units()[unit_class]
        heroes['player'] = PlayerUnit(name, unit, weapon, armor)
        return redirect('/choose-enemy/')


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    # TODO кнопка выбор соперников. 2 метода GET и POST
    # TODO также на GET отрисовываем форму.
    # TODO а на POST отправляем форму и делаем редирект на начало битвы

    if request.method == 'GET':
        return render_template('hero_choosing.html', result=result_choice_enemy)
    elif request.method == 'POST':
        name = request.form.get('name')
        unit_class = request.form.get('unit_class')
        weapon = request.form.get('weapon')
        armor = request.form.get('armor')
        unit = units.get_units()[unit_class]
        heroes['player'] = EnemyUnit(name, unit, weapon, armor)
        return redirect('/fight/')


if __name__ == "__main__":
    app.run(debug=True)
