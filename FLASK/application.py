from flask import Flask, request
from flask import render_template
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
# App para hacer TO-DOs

@application.post('/create-todo')
def create_todo():
    data = request.data
    #quitarle la b
    data = data.decode()
    print(data)


@application.route('/get-todos')
def get_todos():
    return[{"id":1,"todo":"todo1","completed":True},
           {"id":2,"todo":"todo2","completed":True},
           {"id":3,"todo":"todo3","completed":True}]

@application.put('/complete-todo')
def complete_todo():
    pass
