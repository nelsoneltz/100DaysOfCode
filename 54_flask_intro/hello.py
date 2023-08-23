from flask import Flask

# CREATE ENVIROMENT VARIABLE = $env:FLASK_APP = "hello.py"
# CREATE LOCAL FLASSK SERVER = flask run (must be in the same directory of hello.py)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()
