from src.Router import Router
import os
class Header:
    def get_headers():
        OPENROUTER_API_KEY = Router.returnApiKey()
        
        referer = os.environ.get("REFERER", "http://localhost:5000")
    
        return {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "Referer" : referer,
        "X-Title" : "Mi Chatbot Flask"
        }