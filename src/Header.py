class Header:
    @staticmethod
    def get_headers():
        from src.Router import Router
        api_key = Router.returnApiKey()
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Referer": "https://chatbot-l99s.onrender.com",
            "X-Title": "Mi Chatbot Flask"
        }