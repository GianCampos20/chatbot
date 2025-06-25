from flask import Flask, render_template, request, jsonify
import requests
import logging
import sys
from src.Router import Router
from src.Header import Header
from src.Data_Bot import Data_Bot
from dotenv import load_dotenv
load_dotenv()
import os

# Configurar logs para Render (stdout)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

app = Flask(__name__)

OPENROUTER_BASE_URL = Router.baseUrl()

def get_bot_response(message):
    
    headers = Header.get_headers()
    data = Data_Bot.get_data(message)

    try:
        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers=headers,
            json=data
        )
    except requests.exceptions.RequestException as e:
        return "Error al enviar la solicitud"

    if response.status_code != 200:
        print("Codigo de estado: ", response.status_code)
        print("Respuesta: ", response.text)
        return "Error en la respuesta del bot"

    try:
        return response.json()["choices"][0]["message"]["content"]
    except ValueError as e:
        return "Error al procesar la respuesta del bot"

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.json.get("message")
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
