import os
class Router:
    
    @staticmethod
    def returnApiKey():
        
        return os.getenv("OPENROUTER_API_KEY")
    
    @staticmethod
    def baseUrl():
        return "https://openrouter.ai/api/v1"