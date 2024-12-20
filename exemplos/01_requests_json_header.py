import requests;

url = 'https://api.coinbase.com/v2/prices/spot'
cabecalho = {
    "Accept": "application/json",
    "User-Agent": "MinhaAplicacao/1.0"    
}

parametros = {'currency': "USD"}; # Moeda de Consulta


resposta = requests.get(url, params=parametros, headers=cabecalho);
dados = resposta.json();
print(f"Preço do Bitcoin (USD): ", dados['data']['amount']);