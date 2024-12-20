import requests;
import json;
import os;
from dotenv import load_dotenv;

load_dotenv()

url = 'https://api.openai.com/v1/chat/completions';

openai_key = os.getenv('OPENAI_API_KEY');

headers = {
    "content-type": "application/json",
    "Authorization": f"Bearer {openai_key}"
}

data = {    
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": "Qual é a capital da França?"
        }
    ]
}

resposta = requests.post(url, headers=headers, data=json.dumps(data));

print(resposta.json()['choices'][0]['message']['content']);