
from flask import Flask, jsonify, abort, request, render_template

app = Flask(__name__)
lista = [{"nombre": "asdf", "contrasenya": "67890","correo": "asdf@asfd.as", "nacimiento": "12/12/01"},
             {"nombre": "hjkl", "contrasenya": "12345","correo": "hjkl@asfd.as", "nacimiento": "12-12-01"},
             {"nombre": "qwer", "contrasenya": "45678","correo": "qwer@asfd.as", "nacimiento": "12-12-01"},
             {"nombre": "zxcv", "contrasenya": "12345","correo": "zxcv@asfd.as", "nacimiento": "12-12-01"},
             {"nombre": "bnmj", "contrasenya": "12580","correo": "bnmj@asfd.as", "nacimiento": "12-12-01"}]
@app.route("/visual")
def visual():
    return lista

@app.route("/detalle/<string:nombre>")
def detalle(nombre):
    for registro in lista:
        if nombre==registro.get("nombre"):
            return registro

@app.route("/registro/<string:nombre>/<string:contrasenya>/<string:correo>/<string:fecha>")
def registro(nombre,contrasenya,correo,fecha):
    lista.append({"nombre":nombre,"contrasenya":contrasenya,"correo":correo,"fecha":fecha})
    for registro in lista:
        if nombre == registro.get("nombre"):
            return registro