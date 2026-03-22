from web import app
from flask import render_template, request, redirect
from web.models import *
from web.services import convertir
from datetime import datetime

@app.route("/")
def index():
    movimientos = select_all()
    return render_template("index.html", movimientos=movimientos)

@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    if request.method == "POST":
        from_moneda = request.form["from_moneda"]
        to_moneda = request.form["to_moneda"]
        from_cantidad = float(request.form["from_cantidad"])
        boton = request.form["boton"]
        if from_moneda == to_moneda:
            return render_template("purchase.html", error="Las monedas deben ser diferentes")

        if from_moneda != "EUR":
            saldo = saldo_cripto(from_moneda)
            if saldo < from_cantidad:
                return render_template("purchase.html", error="Saldo insuficiente")
            
        if boton == "calcular":
            to_cantidad = convertir(from_cantidad, from_moneda, to_moneda)
            if to_cantidad is None:
                return render_template("purchase.html", error="Error al consultar la API de CoinMarketCap")
            precio_unitario = from_cantidad / to_cantidad
            return render_template("purchase.html",
                from_moneda=from_moneda,
                to_moneda=to_moneda,
                from_cantidad=from_cantidad,
                to_cantidad=to_cantidad,
                precio_unitario=precio_unitario)

        elif boton == "aceptar":
            to_cantidad = float(request.form["to_cantidad"])
            fecha = datetime.now().strftime("%Y-%m-%d")
            hora = datetime.now().strftime("%H:%M:%S")
            insert([fecha, hora, from_moneda, from_cantidad, to_moneda, to_cantidad])
            return redirect("/")
    

    return render_template("purchase.html")

@app.route("/status")
def status():
    invertido = total_invertido()
    recuperado = total_recuperado()
    valor_compra = invertido - recuperado

    cartera = obtener_cripto()
    valor_actual = 0
    for cripto, cantidad in cartera.items():
        valor_en_euros = convertir(cantidad, cripto, "EUR")
        valor_actual += valor_en_euros

    return render_template("status.html",
        invertido=invertido,
        recuperado=recuperado,
        valor_compra=valor_compra,
        valor_actual=valor_actual)