from flask import Flask
import random

# CREATE ENVIROMENT VARIABLE = $env:FLASK_APP = "hello.py"
# CREATE LOCAL FLASSK SERVER = flask run (must be in the same directory of hello.py)

app = Flask(__name__)
random_number = random.randint(0,9)
@app.route("/") 
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>"\
           '<img src = "https://media.giphy.com/media/EMBAJjmUMIpB6/giphy.gif">'

@app.route("/<int:number>")
def guess(number):
    if number < random_number:
        return "<h1>Higher, please</h1>"\
            '<img src = "https://media.giphy.com/media/SDi3kPcN4mILsLKgQc/giphy.gif">'
    if number > random_number:
        return "<h1>Lower, please</h1>"\
            '<img src = "https://media.giphy.com/media/g8tLOZ6RWlDvRf5Kfp/giphy.gif">'
    if number == random_number:
        return "<h1>YEAAAAAAAAAAAAAAAAAAAAH!</h1>"\
            '<img src = "https://media.giphy.com/media/RrVzUOXldFe8M/giphy.gif">'





if __name__ == "__main__":
    app.run(debug=True)
