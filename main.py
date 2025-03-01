from flask import Flask, request, render_template, redirect, Blueprint, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    """
    homepage
    """
    return render_template("index.html")