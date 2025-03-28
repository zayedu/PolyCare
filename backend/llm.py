import config
import requests

API_KEY = config.API_KEY
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

spec = {
    "model": "deepseek/deepseek-chat:free",
    "messages": [{"role": "user", "content": "come up with 5 symptom questions to determine if a patient has PCOS"}]
}

response = requests.post(API_URL, json=spec, headers=headers)

if response.status_code == 200:
    print("API Response:", response.json())
else:
    print("Failed. Status Code:", response.status_code)