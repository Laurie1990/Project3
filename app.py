import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from flask import Flask, jsonify, render_template, request
from joblib import load
#from models.persist import load_model



app= Flask(__name__)


@app.route('/index')
def index():
    """
    Display the main webpage where users can enter their details
    which we will then pass to the prediction endpoint
    """
    #return "Testing, testing"
    return render_template("Index.html")

# @app.route('/predict_test')
# def predict_test():
#     # model=load_model()
#     # X, y= load_data()
#     # X_train, X_test, y_train, y_test = split_data(X,y)
#     # report=test_model(model, X_train, y_train)

#     # return jsonify(report)

# #=========================================================================================#
#     model = load_model()

#     # convert nparray to list so we can
#     # serialise as json
#     result = model.predict(X).tolist()

#     return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

