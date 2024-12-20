import requests;

url = 'https://jsonplaceholder.typicode.com/comments';
parametros = {'postId': 1};
resposta = requests.get(url, params= parametros);

dados = resposta.json();
print(f"Foram encontrados {len(dados)} comentários.");
print(f"Erro: {resposta.status_code} - {resposta.text}");