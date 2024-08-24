from flask import Flask

from flask_restx.apidoc import apidoc


ROOT_URL = '/sample_project'


def create_app(config_name):
    from sample_project.config import app_config

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["APPLICATION_ROOT"] = ROOT_URL

    """
    Flask-RESTPlus uses `apidoc` to generate URLs for static files in Swagger UI.

    To ensure proper routing, consider the following:
    1. If `apidoc` is not registered as a blueprint (the default case).
    2. If `apidoc` is registered after another blueprint.

    In these cases, Flask-RESTPlus automatically registers the default `apidoc` at the root path (`/`).

    Therefore,it is recommended that `apidoc` be the first blueprint registered, ensuring it is mounted at `ROOT_URL`.
    """

    app.register_blueprint(apidoc, url_prefix=ROOT_URL)

    with app.app_context():
        from sample_project.api_v1 import blueprint as api
        from sample_project.healthcheck import healthcheck

        app.register_blueprint(api, url_prefix=ROOT_URL + '/api/v1.0')
        app.register_blueprint(healthcheck, url_prefix=ROOT_URL + '/version')
    return app
