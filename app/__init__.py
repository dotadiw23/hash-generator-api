from flask import Flask

from app.urls import register_apis


def create_app(name: str) -> Flask:
    """
    :param (str) name:
        Nombre de la app
    :return:
        (Flask) Objeto de app de Flask
    """
    app = Flask(name)
    register_apis(app)
    return app
