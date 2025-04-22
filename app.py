from flask import Flask, render_template, request, jsonify
import requests
import os
from src.Router import Router
from src.Header import Header
from src.Data_Bot import Data_Bot

app = Flask(__name__)

OPENROUTER_API_KEY = Router.returnApiKey()
OPENROUTER_BASE_URL = Router.baseUrl()

def get_bot_response(message):
     
     headers = Header.get_headers()
     
     data = Data_Bot.get_data(message)
     
     response = requests.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=data)
     
     if not response.status_code == 200:
         
        print(f"Error: {response.status_code}, Response: {response.text}")
    
        return "Error en la respuesta del bot"
        
     return response.json()["choices"][0]["message"]["content"]
     
@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/send", methods=["POST"])
def send():
    user_message = request.json.get("message")
    bot_response = get_bot_response(user_message)
    return jsonify({"response" : bot_response})


if __name__ == "__main__":
    app.run(debug=True)