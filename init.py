from flask import Flask, render_template
from DBConnect import connectToDB
Connection = connectToDB()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html",Connection = Connection)

if __name__ == "__main__":
    app.run()
