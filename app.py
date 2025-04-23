from flask import Flask, render_template, request, jsonify
import requests
import logging
import sys

from src.Router import Router
from src.Header import Header
from src.Data_Bot import Data_Bot

# Configurar logs para Render (stdout)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

app = Flask(__name__)

OPENROUTER_API_KEY = Router.returnApiKey()
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
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response text: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        return "Error al enviar la solicitud"

    if response.status_code != 200:
        logging.error(f"Error en la respuesta del bot: {response.text}")
        return "Error en la respuesta del bot"

    try:
        return response.json()["choices"][0]["message"]["content"]
    except ValueError as e:
        logging.error(f"Error al procesar JSON: {e}")
        return "Error al procesar la respuesta del bot"

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.json.get("message")
    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

# Ruta de prueba de conexión
@app.route("/test-connection", methods=["GET"])
def test_connection():
    try:
        response = requests.get("https://httpbin.org/get")
        return jsonify({"status": "success", "data": response.json()})
    except requests.exceptions.RequestException as e:
        logging.error(f"Error en test-connection: {e}")
        return jsonify({"status": "error", "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
