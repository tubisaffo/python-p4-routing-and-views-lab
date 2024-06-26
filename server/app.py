from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(f"{param}")
    return param

@app.route('/count/<int:param>')
def count(param):
    numbers = [i for i in range(int(param))]
    return "\n".join(map(str, numbers)) + '\n' 

@app.route('/math/<int:param1>/<string:operation>/<int:param2>')
def math(param1, operation, param2):
    if operation == "+":
        return str(param1 + param2)
    elif operation == "-":
        return str(param1 - param2)
    elif operation == "*":
        return str(param1 * param2)
    elif operation == "div":
        return str(param1 / param2)
    elif operation == "%":
        return str(param1 % param2)

if __name__ == '__main__':
    app.run(debug=True)
