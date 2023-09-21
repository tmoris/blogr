# Importing  module
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from blog.models import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)

    # Secret key cofig
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    # Database Config
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URI

    # Initialize database
    db.init_app(app)
    bcrypt = Bcrypt(app)

    # Initialize and create instance of LoginManger
    login_manager = LoginManager(app)
    login_manager.login_view = "views.login"
    login_manager.login_message_category = "info"
    # Mail configurations
    app.config["MAIL_SERVER"] = "smtp.googlemail.com"
    app.config["MAIL_PORT"] = "587"
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = os.environ.get("USER_EMAIL")
    app.config["MAIL_PASSWORD"] = os.environ.get("PASS")

    from blog.models import User, Post

    # Register Blueprints
    from blog.views import bp as veiws_bp

    app.register_blueprint(veiws_bp)

    # Userloader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
    return app
