# Import libraries
# import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd


app = Flask(__name__)
# app = Flask(__name__, template_folder='app')


# Load the model
model = pickle.load(open('Model- sav/logisticregression.sav','rb'))
print(model)

@app.route("/")
def home():
    return render_template("app/index.html")


if __name__ == "__main__":
    app.run(debug=True)