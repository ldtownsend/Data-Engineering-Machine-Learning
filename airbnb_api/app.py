"""
App factory to create AirBnB price prediction API

__author__ = Patrick Dugovich, Xander Bennett, Andrew Archie, Luke Townsend
__license__ = MIT License
__version__ = 1.0

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

            neighbourhood_group_cleansed = request.args.get('neighbourhood_group_cleansed')
            request_data.update(neighbourhood_group_cleansed=neighbourhood_group_cleansed)
            bathrooms = request.args.get('bathrooms')
            request_data.update(bathrooms=bathrooms)
            bedrooms = request.args.get('bedrooms')
            request_data.update(bedrooms=bedrooms)
            beds = request.args.get('beds')
            request_data.update(beds=beds)
            bed_type = request.args.get('bed_type')
            request_data.update(bed_type=bed_type)
            amenities = request.args.get('amenities')
            request_data.update(amenities=amenities)
            room_type = request.args.get('room_type')
            request_data.update(room_type=room_type)
            cleaning_fee = request.args.get('cleaning_fee')
            request_data.update(cleaning_fee=cleaning_fee)
            security_deposit = request.args.get('security_deposit')
            request_data.update(security_deposit=security_deposit)
            minimum_nights = request.args.get('minimum_nights')
            request_data.update(minimum_nights=minimum_nights)
            # for param in parameters:
            #     request_data.update(param = request.args.get(param))
 
            print('request_data:', request_data)

            # Turning data into pandas DataFrame for use in model
            data_df = pd.DataFrame(request_data, index=[1])
            print('data_df:',data_df)

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
