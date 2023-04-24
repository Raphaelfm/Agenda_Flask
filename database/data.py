import json
import mysql.connector

# Lê as informações de conexão do arquivo config.json
with open('config.json') as f:
    config = json.load(f)

def conectar():
    # Conecta ao banco de dados usando as informações do arquivo JSON
    return mysql.connector.connect(
        host=config['mysql']['host'],
        port=config['mysql']['port'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database']
    )
