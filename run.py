from flask import Flask
from flask_cors import CORS
from PromoPilot import chat
from PromoPilot.views import socketio
from decouple import config
from extensions import db


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = config('SECRET_KEY')
    app.config.from_object('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(chat)
    socketio.init_app(app)
    return app


if __name__ == '__main__':
    app_instance = create_app()
    socketio.run(app_instance, host='0.0.0.0', port=5001, debug=True, use_reloader=True)
