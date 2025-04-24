import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')
class Router:
    
    @staticmethod
    def returnApiKey():
        load_dotenv()  # Asegúrate de que las variables se carguen antes de acceder a ellas
        api_key = os.getenv("OPENROUTER_API_KEY")
        print(f"API Key cargada: {api_key}")  # Verifica si el valor es el esperado
        return api_key
    
    @staticmethod
    def baseUrl():
        return "https://openrouter.ai/api/v1"