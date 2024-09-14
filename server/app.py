#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<string:parameter>')
def count(parameter):
    count_range = range(int(parameter))
    count_list = ""
    for num in count_range:
        count_list = f'{count_list}{num}\n' 
       
    print(count_list)
    return count_list

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    print(num1, num2, operation)
    num1_num = int(num1)
    num2_num = int(num2)
    if operation == "+":
        return f"{num1_num + num2_num}"
    elif operation == "-":
        return f"{num1_num - num2_num}"
    elif operation == "*":
        return f"{num1_num * num2_num}"
    elif operation == "div":
        return f"{num1_num / num2_num}"
    elif operation == "%":
        return f"{num1_num % num2_num}"
    else:
        return 'invalid'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
