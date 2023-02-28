from flask import Flask, abort, redirect, url_for, request, render_template, json
import re
app = Flask(__name__)

lista = [{"id":1,"nombre": "asdf", "contrasenya": "67890", "correo": "asdf@asfd.as", "isPremium": True},
         {"id":2,"nombre": "hjkl", "contrasenya": "12345", "correo": "hjkl@asfd.as", "isPremium": False},
         {"id":3,"nombre": "qwer", "contrasenya": "45678", "correo": "qwer@asfd.as", "isPremium": True},
         {"id":4,"nombre": "zxcv", "contrasenya": "12345", "correo": "zxcv@asfd.as", "isPremium": False},
         {"id":5,"nombre": "bnmj", "contrasenya": "12580", "correo": "bnmj@asfd.as", "isPremium": True},
         {"id":6,"nombre": "agustin", "contrasenya": "1234", "correo": "bnmj@asfd.as", "isPremium": False}]


@app.route("/get-all-users")
def getAll():
    return lista
@app.route("/login", methods=["POST"])
def login():
    #for logeo in lista:
    if request.method == 'POST':
        user = json.loads(request.data.decode('utf-8'))
        passw = json.loads(request.data.decode('utf-8'))
        for usuario in lista:
            if user == usuario.get("nombre") and passw== usuario.get("contrasenya"):
                return "<p>usuario logueado</p>" % user % passw
            else:
                abort(404)
    else:
        abort(404)

@app.route("/get-user")
def getUsuario():
    id = request.args.get("id")

    for usuario in lista:
        if int(id) == usuario.get("id"):
            return usuario
        else:
            abort(404)

@app.route("/new-user", methods=["GET"])
def newUser(username,password,email,dni,isPremium):

    pass

@app.errorhandler(404)
def error_404_handler(e):
    return "ERROR 404", 404

@app.errorhandler(401)
def error_404_handler(e):
    return "ERROR usuario ya existente", 401
