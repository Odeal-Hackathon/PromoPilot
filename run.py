from flask import Flask
from flask_cors import CORS
from PromoPilot import chat
from PromoPilot.views import socketio
from decouple import config


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = config('SECRET_KEY')
    app.register_blueprint(chat)
    socketio.init_app(app)
    return app


if __name__ == '__main__':
    app_instance = create_app()
    socketio.run(app_instance, port=5004, debug=True, allow_unsafe_werkzeug=True)
