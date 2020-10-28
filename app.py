import pandas as pd
from flask import Flask, jsonify, render_template, request
from joblib import load
app= Flask(__name__)


@app.route('/')
def index():
    """
    Display the main webpage where users can enter their details
    which we will then pass to the prediction endpoint
    """
    return render_template("index.html")