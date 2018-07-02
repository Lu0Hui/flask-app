from flask import Flask


def create_app():
    app = Flask(__name__)

    from apps.core.views import core as core_blueprint
    app.register_blueprint(core_blueprint, url_prefix='/')

    return app
