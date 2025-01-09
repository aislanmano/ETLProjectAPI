from sqlalchemy import *
from sqlalchemy.dialects import * 
from sqlalchemy.orm import declarative_base 
from sqlalchemy import column, Integer, String, Float, DateTime
from datetime import datetime

#Cria a classe Base do SQLAlchemy (na versão 2.x)
Base = declarative_base()

class BitcoinPreco(Base):
    """Define a tabela no banco de dados."""
    __tablename__ = 'bitcoin_precos'
    
    id =            column(Integer, primary_key=True, autoincrement=True)
    criptomoeda =   column(String(50), nullable=False)
    moeda =         column(String(10), nullable=False)
    valor =         column(Float, nullable=False)
    timestamp =     column(DateTime, default=datetime.now)