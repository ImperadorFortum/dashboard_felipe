import sqlite3

FILE_DB ='./database/database.db '

def connect():
    """ Cria a conexão com o banco de dados"""

    conn = sqlite3.connect(FILE_DB)
    return conn
