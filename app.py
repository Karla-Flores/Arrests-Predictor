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
@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


# @app.route('/predict', methods=["GET", "POST"])
# def predict():

#     if request.method == "POST": 

#     # predicting fatal or non-fatal with our model
#         modelfile = 'Model/logisticregression.pickle'
#         model = p.load(open(modelfile, 'rb'))
#         predict = model.predict()

#     return render_template("index.html", pred = predict[0])





# @app.route('/predict', methods=["GET", "POST"])
# def predict():
# # GET request
#     if request.method == 'GET':
#         message = {'greeting':'Hello from Flask!'}
#         return jsonify(message)  
#     # # serialize and use JSON headers

#     # POST request
#     if request.method == 'POST':
#         print(request.get_json())  # parse as JSON
#         return 'Sucesss', 200
    
#     return render_template("index.html")

# @app.route('/api',methods=['POST'])
# def predict():
#     # Get the data from the POST request.
#     data = request.get_json(force=True)
#     # Make prediction using model loaded from disk as per the data.
#     prediction = model.predict([[np.array(data['exp'])]])
#     # Take the first value of prediction
#     output = prediction[0]
#     return jsonify(output)




if __name__ == "__main__":
    app.run(debug=True)