from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    motorizacao = Column(String)
    combustivel = Column(String)
    cor = Column(String)
    quilometragem = Column(Integer)
    portas = Column(Integer)
    transmissao = Column(String)
    preco = Column(Float)
