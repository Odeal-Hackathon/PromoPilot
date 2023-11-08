from flask import current_app, render_template, session
from sqlalchemy import MetaData
from flask_socketio import SocketIO
from jinja2 import Template

from api.customer_lookup import customer_lookup
from api.odeal_retiew import retrieve_documentation
from . import chat
from .controllers import Settings, ChatSession, RequestManager
import logging
from .models import Odeal, db
import os
import openai
from decouple import config

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
        doc_result = retrieve_documentation(message)
        cust_info = customer_lookup(selection)
        #bot_response = manager.send_request(message, selection)
        session['cust_info'] = cust_info
        session['doc_result'] = doc_result
        session['customer_id'] = selection
        session['question'] = message

        print(session['cust_info'])
        print(session['doc_result'])
        print(session['customer_id'])
        print(session['question'])
        template = user_prompt_template()
        bot_response = llm_model(template)
        print('REEESSPOONNNSSSEEE')
        print(bot_response)
        #bot_response = 'cevap'
    except ConnectionError:
        bot_response = "Bir hata oluştu. Lütfen tekrar deneyin."

    socketio.emit('bot_response', bot_response)


def user_prompt_template():
    with open('/Users/seymasarigil/Github/PromoPilot/templates/user_prompt.j2', 'r', encoding='utf-8') as file:
        prompt_template = file.read()
    template = Template(prompt_template)

    params = {
        'customer_id': session['customer_id'],
        'customer_information': session['cust_info'],
        'documentation': session['doc_result'],
        'question': session['question']
    }

    rendered_prompt = template.render(params)
    return rendered_prompt


def llm_model(message_text):

    openai.api_type = "azure"
    openai.api_base = config('AZURE_API_BASE')
    openai.api_version = "2023-07-01-preview"
    openai.api_key = config("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-4-32k",
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    result = completion.response()
    return result