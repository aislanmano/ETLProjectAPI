import requests
from tinydb import TinyDB
from datetime import datetime

# Extraindo dados - EXTRACT
def extract_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

# Transformando dados - TRANSFORM
def transform_dados_bitcoin(dados):
    valor =         dados['data']['amount']
    criptomoeda =   dados['data']['base']
    moeda =         dados['data']['currency']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    dados_transformados = {        
        'criptomoeda': criptomoeda,
        'moeda': moeda,
        'valor': valor,
        'timestamp': timestamp
    }
    
    return dados_transformados

# Salvando dados - LOAD
def salvar_dados_tinydb(dados, dbname="bitcoin.json"):
    db = TinyDB(dbname)
    db.insert(dados)
    print("Dados salvos com sucesso!")
      
if __name__ == '__main__':
    dados_json = extract_dados_bitcoin()
    dados_transformados = transform_dados_bitcoin(dados_json)
    salvar_dados_tinydb(dados_transformados)