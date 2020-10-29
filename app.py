import pandas as pd
from flask import Flask, jsonify, render_template, request
from joblib import load
from model.persist import load_model



app= Flask(__name__)


@app.route('/')
def index():
    """
    Display the main webpage where users can enter their details
    which we will then pass to the prediction endpoint
    """
    return render_template("index.html")

@app.route('/predict_test')
def predict_test():



if __name__ == '__main__':
    app.run()

