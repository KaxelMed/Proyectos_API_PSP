from flask import Flask, request

aplication = Flask(__name__)

@aplication.route('/')
def hello_world():
    print(request.method)
    return "<h1>Hello world</h1>"