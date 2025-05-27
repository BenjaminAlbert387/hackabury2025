from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def entry():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)