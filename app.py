# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd


# app = Flask(__name__)
app = Flask(__name__, template_folder='app')


# Load the model
model = pickle.load(open('Model- sav/logisticregression.sav','rb'))
print(model)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api_list():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
    )

@app.route('/predict',methods=['POST'])
def predict():
    filter = request.form['user-input']
    # use your pickled model with the user input
    # to generate a new prediction
    return "hello world" # really, you'll want to return a template with the predictions


if __name__ == "__main__":
    app.run(debug=True)