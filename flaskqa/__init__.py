from flask import Flask
from .commands import create_tables
from .extensions import db, login_manager
from .models import User
from .routes.auth import auth
from .routes.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    app.secret_key = b'\x10\x06@.\xcb\xac\xdb\xa7\xe8\x8d\xedi\x80O\ta.\xcc\x8a\x03&\x10C&'

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    app.cli.add_command(create_tables)

    return app