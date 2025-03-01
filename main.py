from flask import Flask, request, render_template, redirect, Blueprint, jsonify 
from database import Databases

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    """
    homepage
    """
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
