import os

from flask import Flask
from dotenv import load_dotenv
from src.main.main import main
from src.auth.auth import auth

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.register_blueprint(main)

    app.register_blueprint(auth)

    return app

if __name__ == '__main__':
    apps = create_app()
    apps.run(debug=True)