"""
App factory to create AirBnB price prediction API

__author__ = Patrick Dugovich, Xander Bennett, Luke Townsend
__license__ = MIT License
__version__ = 1.1

"""
from .data_cleaning import wrangle
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import pickle


def create_app():
    # app
    app = Flask(__name__)
    # CORS to try to prevent errors with web end
    CORS(app)

    # Loading model extracted from notebook
    model = pickle.load(open('model.pkl', 'rb'))

    parameters = [
        'neighbourhood_group_cleansed', 'bathrooms', 'bedrooms',
        'beds', 'bed_type', 'amenities', 'room_type', 'cleaning_fee',
        'security_deposit', 'minimum_nights'
    ]

    # routes
    @app.route('/', methods=['GET'])
    def predict():
        try:
            request_data = {}
            
            # For loop to populate dictionary with parameters from request
            for param in parameters:
                request_data.update({param: request.args.get(param)})

            # This print statement is used for debugging.
            print('request_data:', request_data)

            # Turning data into pandas DataFrame for use in model
            data_df = pd.DataFrame(request_data, index=[1])

            # This print statement is used when debugging
            print('data_df:', data_df)

            # Adding individual columns for each amenity
            data_df = wrangle(data_df)

            # Make prediction based on created dataframe of user input data
            result = model.predict(data_df)

            # Creating dict to convert to json and return
            output = int(result[0])

            request_data.update(estimated_price=output)

            return jsonify(request_data)

        except Exception as e:
            return jsonify({'Error': e})

    return app
