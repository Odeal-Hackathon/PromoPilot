from flask import current_app, render_template
from sqlalchemy import MetaData
from flask_socketio import SocketIO
from . import chat
from .controllers import Settings, ChatSession, RequestManager
import logging
from .models import Odeal, db

logging.basicConfig(level=logging.DEBUG)

socketio = SocketIO(cors_allowed_origins="*", logger=True, engineio_logger=True)

settings = Settings()
chat_session = ChatSession()
manager = RequestManager(settings, chat_session)


@chat.route('/dbtest')
def dbtest():
    try:
        with current_app.app_context():
            meta = MetaData()
            meta.reflect(bind=db.engine)
            tables = list(meta.tables.keys())
            return f"Bağlantı başarılı! Tablolar: {tables}"
    except Exception as e:
        return f"Bağlantı hatası: {str(e)}"


@chat.route('/')
def index():
    distinct_brands = Odeal.query.with_entities(Odeal.id, Odeal.Marka).distinct(Odeal.Marka).all()
    return render_template('index.html', brands=distinct_brands)


@socketio.on('user_message')
def handle_user_message(data):
    print("Message received:", data['message'])
    print("Dropdown selection:", data['dropdownValue'])
    message = data['message']
    selection = data['dropdownValue']
    try:
        bot_response = manager.send_request(message, selection)
        #bot_response = 'cevap'
    except ConnectionError:
        bot_response = "Bir hata oluştu. Lütfen tekrar deneyin."

    socketio.emit('bot_response', bot_response)
