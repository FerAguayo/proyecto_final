import sqlite3
from config import DATA_ORIGIN

class Conexion:
    def __init__(self, query_sql, parametros=[]):
        self.con = sqlite3.connect(DATA_ORIGIN)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(query_sql, parametros)