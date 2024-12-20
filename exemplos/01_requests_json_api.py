import requests;
import json;

url = 'https://api.openai.com/v1/chat/completions';

headers = {
    "content-type": "application/json",
    "Authorization": "Bearer xxxxxxxx"
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