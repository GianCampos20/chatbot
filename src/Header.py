class Header:
    @staticmethod
    def get_headers():
        from src.Router import Router
        api_key = Router.returnApiKey()
        print("🧪 Usando API Key:", api_key[:10] + "...")  # para debug
        return {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }