from flask import Blueprint, render_template

menu_blueprint = Blueprint('menu_blueprint', __name__, template_folder='./templates')


@menu_blueprint.get("/")
def menu_page():
    return render_template('index.html')
