# Put your app in here.
from operations import *
from flask import Flask, request

app = Flask(__name__)
operations = {"add": add, "sub": sub, "mult": mult, "div": div}

@app.route('/add')
def add_numbers():
    '''Adds two numbers provided in URL'''
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route('/sub')
def subtract_numbers():
    '''Subtracts two numbers provided in URL'''
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route('/mult')
def mult_numbers():
    '''Multiplies two numbers provided in URL'''
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route('/div')
def div_numbers():
    '''Divides two numbers provided in URL'''
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

@app.route('/math/<op>')
def do_math(op):
    '''Does a math operation (add, sub, mult, div) with numbers (all specified in URL)'''
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations[op](a, b))
