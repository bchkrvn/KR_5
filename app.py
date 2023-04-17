from flask import Flask


from views.choose import choose_blueprint
from views.fight import fight_blueprint
from views.menu import menu_blueprint


def create_app():
    application = Flask(__name__)
    application.register_blueprint(menu_blueprint)
    application.register_blueprint(choose_blueprint)
    application.register_blueprint(fight_blueprint, url_prefix='/fight')

    return application


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
