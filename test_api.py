import requests

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization" : f"Bearer {API_KEY}",
    "Content-type" : "application/json"
}

data = {
    "model" : "openai/gpt-3.5-turbo",
    "messages" : [
        {
            "role" : "user",
            "content": "Hola, como estas?"
        }
    ]
}

response = requests.post(API_URL, headers=headers, json=data)

print("Status code: ", response.status_code)
print("Response Body: ", response.text)