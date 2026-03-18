from web import app
from flask import render_template
from web.models import *

@app.route("/")
def index():
    movimientos = select_all()
    return render_template("index.html", movimientos=movimientos)