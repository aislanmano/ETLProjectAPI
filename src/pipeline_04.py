import os
import time
import requests
import logging
import logfire
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from logging import getLogger, basicConfig


# Configuração LogFire
logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = getLogger(__name__)
logger.setLevel(logging.INFO)
logfire.instrument_requests()
logfire.instrument_sqlalchemy()

# Importa as classes do arquivo database.py
from database import Base, BitcoinPreco

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv('POSTGRES_USER') 
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST') 
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# cria a engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    logger.info("Tabela criada/verificada com sucesso!")

def extract_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase"""
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.json()
    else:
        logger.error(f"Erro na requisição: {resposta.status_code}")
        

def transform_dados_bitcoin(dados):
    valor = dados['data']['amount']
    criptomoeda = dados['data']['base']
    moeda = dados['data']['currency']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    dados_transformados = {        
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": timestamp
    }
    
    return dados_transformados

def salvar_dados_postgresql(dados):
    """Salva os dados no banco de dados PostgreSQL."""
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    logger.info(f"[{dados['timestamp']}] Dados salvos no PostgreSQL com sucesso!")
      
if __name__ == '__main__':
    criar_tabela()
    logger.info("Iniciando ETL com atualização a cada 10 segundos... (CTRL+C para interromper)")
    
    while True:
        try:            
            dados_json = extract_dados_bitcoin()
            if dados_json:
                dados_transformados = transform_dados_bitcoin(dados_json)
                logger.info("Dados tratados: ", dados_transformados)
                salvar_dados_postgresql(dados_transformados)
                time.sleep(10)
        except KeyboardInterrupt:
            logger.info("\nProcesso ETL interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            logger.info(f"Erro durante a execução: {e}")
            time.sleep(10)
        



