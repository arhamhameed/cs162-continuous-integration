import requests
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, mapper

# POST HTTP request with valid expression
r = requests.post('http://192.168.99.100:5000/add', data = {'exp': '1+2+3'})

DB_URI = 'postgres+psycopg2://user:password@192.168.99.100:5432'
engine = create_engine(DB_URI)

session = sessionmaker(bind=engine)

metadata = MetaData(engine)
expressions = Table('expression', metadata, autoload=True)
mapper(Exps, expressions)

s = session()

# POST HTTP request with an invalid expression
r1 = requests.post('http://192.168.99.100:5000/add', data = {'exp': '1+b+3'})

