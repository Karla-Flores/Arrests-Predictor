# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pickle as p
import pandas as pd


# app = Flask(__name__)
app = Flask(__name__, template_folder='app')


# Load the model
# model = pickle.load(open('Model- sav/logisticregression.pickle','rb'))
# print(model)

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
        f"Available Routes:<br>"
        f"Here goes some api"
    )

@app.route('/results/<crime>/<location>/<season>/<hour>/<lat>/<lon>/<domestic>')
def results(crime,location,season,hour,lat,lon,domestic):
    
    data = np.array([crime,location,season,hour,lat,lon,domestic]).reshape(1,-1)
    output = model.predict(data)
    
    return jsonify({'result':output})


if __name__ == "__main__":
    app.run(debug=True)