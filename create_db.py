from web.conexion import Conexion

with open("data/create.sql", "r") as f:
    sql = f.read()

connect = Conexion(sql)
connect.con.commit()
connect.con.close()