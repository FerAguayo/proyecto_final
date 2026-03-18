from web.conexion import Conexion

def select_all():
    connect = Conexion("SELECT * FROM movimientos;")
    
    filas = connect.res.fetchall()
    columnas = connect.res.description
    
    lista_diccionario = []
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion += 1
        lista_diccionario.append(diccionario)
    
    connect.con.close()
    
    return lista_diccionario

def insert(datos_form):
    connectInsert = Conexion(
        "INSERT INTO movimientos(date, time, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?,?);",
        datos_form
    )
    connectInsert.con.commit()
    connectInsert.con.close()

def saldo_cripto(cripto):
    connectEntrada = Conexion("SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to = ?;", [cripto])
    entrada = connectEntrada.res.fetchall()[0][0]
    connectEntrada.con.close()
    entrada = entrada or 0
    
    connectSalida = Conexion("SELECT SUM(cantidad_from) FROM movimientos WHERE moneda_from =?", [cripto])
    salida= connectSalida.res.fetchall() [0][0]
    connectSalida.con.close()
    salida = salida or 0
    return entrada - salida

def total_invertido():
    connectInvertido = Conexion("SELECT SUM(cantidad_from) FROM movimientos WHERE moneda_from = 'EUR';")
    invertido = connectInvertido.res.fetchall()
    connectInvertido.con.close()
    invertido = invertido or 0
    return invertido

def total_recuperado():
    connectRecuperado = Conexion("SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to = 'EUR';")
    recuperado = connectRecuperado.res.fetchall()
    connectRecuperado.con.close()
    recuperado = recuperado or 0
    return recuperado

def obtener_cripto():
    connectDistintas_to = Conexion("SELECT DISTINCT moneda_to FROM movimientos WHERE moneda_to != 'EUR';")
    distintas_to = connectDistintas_to.res.fetchall()
    connectDistintas_to.con.close()
    
    connectDistintas_from = Conexion("SELECT DISTINCT moneda_from FROM movimientos WHERE moneda_from !='EUR';")
    distintas_from = connectDistintas_from.res.fetchall()
    connectDistintas_from.con.close()
    
    todas = set()
    for fila in distintas_to:
        todas.add(fila[0])
    for fila in distintas_from:
        todas.add(fila[0])
    
    cartera = {}
    for cripto in todas:
        saldo = saldo_cripto(cripto)
        if saldo > 0:
            cartera[cripto] = saldo
    return cartera

