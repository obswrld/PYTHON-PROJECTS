from flask import Flask
from dotenv import load_dotenv
from src.main import main
from src.auth import auth

load_dotenv()

def create_app():
    apps = Flask(__name__)

    apps.register_blueprint(main)

    apps.register_blueprint(auth)

    return apps

if __name__ == '__main__':
    app = create_app()
    app.run()
    app.run(debug=False)