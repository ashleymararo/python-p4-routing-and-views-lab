#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# 1️⃣ Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


# 2️⃣ Print string route
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param


# 3️⃣ Count route
@app.route('/count/<int:num>')
def count(num):
    result = ""
    for i in range(num):
        result += f"{i}\n"
    return result


# 4️⃣ Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'