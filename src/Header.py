import os

class Header:
    def get_headers():
        # Usamos la variable de entorno para obtener la API Key
        OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

        # Verificamos si la API key está disponible
        if OPENROUTER_API_KEY is None:
            raise ValueError("La API key no está configurada en las variables de entorno.")
        
        return {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "Referer": "https://chatbot-l99s.onrender.com",
            "X-Title": "Mi Chatbot Flask"
        }