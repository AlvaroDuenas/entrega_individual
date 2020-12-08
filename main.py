import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
# Carga de la aplicacion flask
app = Flask(__name__)
"""
user = os.environ['MONGODB_USERNAME']
password = os.environ['MONGODB_PASSWORD']
db_name = os.environ['MONGODB_DATABASE']

client = MongoClient("mongo:27017",
	username=user,
	password=password,
	authSource=db_name,
	authMechanism='SCRAM-SHA-1')
"""
# Carga del cliente Mongo
client = MongoClient("mongo", 27017)
# Acceso a la base de datos
db = client.appdb

# Pagina principal de la aplicacion
## Corresponde al textlabel y boton para almacenar un nuevo objeto.
@app.route("/")
def index():
## Obtiene las colecciones existentes
    _items = db.appdb.find()
    items = [items for items in _items]
## Muestra el fichero html en el servidor
    return render_template("index.html", items=items)

# Anade la nueva entrada a la base de datos y se redirige a la pagina inicial
@app.route("/new", methods=["POST"])
def new():
## Obtiene el nuevo objeto en formato json
    data = {
        "helloworld": request.form["helloworld"]
    }
## Inserta el objeto en la base de datos
    db.appdb.insert_one(data)
## Redirige la interfaz a la pagina inicial
    return redirect(url_for("index"))
