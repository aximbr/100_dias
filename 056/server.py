import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html" )

@app.route('/index.html')
def get_index():
    return render_template("index.html" )

@app.route('/single.html')
def get_single():
    return render_template("single.html" )

if __name__ == "__main__":
    app.run(debug=True)