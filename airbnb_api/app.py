"""
App factory to create AirBnB price prediction API
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

    # routes
    @app.route('/', methods=['POST'])
    def predict():
        try:
            # Requesting JSON data
            request_data = request.get_json(force=True)

            # Turning data into pandas DataFrame for use in model
            request_data.update((x, [y]) for x, y in request_data.items())
            data_df = pd.DataFrame.from_dict(request_data)

            # Adding individual columns for each amenity
            data_df = wrangle(data_df)

            # Make prediction based on created dataframe of user input data
            result = model.predict(data_df)

            # Creating dict to convert to json and return
            output = int(result[0])

            return jsonify(estimated_price=output)

        except Exception as e:
            return jsonify({'Error': e})

    return app
