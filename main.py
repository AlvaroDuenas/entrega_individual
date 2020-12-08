import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from urllib.parse import quote_plus
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
client = MongoClient("mongo", 27017)
db = client.appdb

@app.route("/")
def index():
    _items = db.appdb.find()
    items = [items for items in _items]

    return render_template("index.html", items=items)


@app.route("/new", methods=["POST"])
def new():
    data = {
        "helloworld": request.form["helloworld"]
    }

    db.appdb.insert_one(data)

    return redirect(url_for("index"))
