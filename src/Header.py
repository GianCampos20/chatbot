from src.Router import Router

class Header:
    def get_headers():
        OPENROUTER_API_KEY = Router.returnApiKey()
    
        return {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "Referer" : "http://localhost:5000",
        "X-Title" : "Mi Chatbot Flask"
        }