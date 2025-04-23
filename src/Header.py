from src.Router import Router
import os
class Header:
    def get_headers():
        # OPENROUTER_API_KEY = Router.returnApiKey()
        
        referer = os.environ.get("REFERER", "http://localhost:5000")
    
        return {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
        "Referer" : referer,
        "X-Title" : "Mi Chatbot Flask"
        }