class Data_Bot:
    
    def get_data(message):
        
        return {
        "model" : "openai/gpt-3.5-turbo-16k",
        "messages" : [
            {"role" : "system", "content" : "Eres un asistente útil y simpático"},
            {"role" : "user", "content" : message}  
        ]
     }