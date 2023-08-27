from flask import Flask

# CREATE ENVIROMENT VARIABLE = $env:FLASK_APP = "hello.py"
# CREATE LOCAL FLASSK SERVER = flask run (must be in the same directory of hello.py)

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function
def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function
def make_underline(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function

@app.route("/") 
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye") 
@make_bold
@make_emphasis
@make_underline
def bye():
    return "<p>Bye!</p>"

@app.route("/username/<name>") # use name as a variable in the page
def greet(name):
    return f'Hello {name}'


if __name__ == "__main__":
    app.run(debug=True)
