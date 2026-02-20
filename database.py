from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["supermercado_db"]

usuarios = db["usuarios"]
produtos = db["produtos"]
vendas = db["vendas"]
