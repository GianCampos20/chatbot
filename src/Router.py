import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')
class Router:
    
    @staticmethod
    def returnApiKey():
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY")
        return api_key
    
    @staticmethod
    def baseUrl():
        return "https://openrouter.ai/api/v1"