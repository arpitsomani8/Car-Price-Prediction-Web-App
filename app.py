# import required packages
from flask import Flask, render_template, request, jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from datetime import date

# create a Flask object
app = Flask("car_model")

# load the ml model which we have saved earlier in .pkl format
model = pickle.load(open('car_price_model.pkl', 'rb'))

# define the route(basically url) to which we need to send http request
# HTTP GET request method
@app.route('/', methods=['GET'])
# create a function Home that will return index.html(which contains html form)
# index.html file is created seperately
def Home():
    return render_template('index.html')


if __name__ == "__main__":
    # run method starts our web service
    # Debug : as soon as I save anything in my structure, server should start again
    app.run(debug=True)
