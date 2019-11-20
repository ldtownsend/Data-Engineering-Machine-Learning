'''Example app.py file. TODO - '''
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import pickle


# app
app = Flask(__name__)
CORS(app)

# Loading the model once it's available
model = pickle.load(open('model.pkl', 'rb'))

# routes
@app.route('/', methods=['POST'])
def predict():
    if model:
        try:
            # Requesting JSON data
            request_data = request.get_json(force=True)

            # Turning data into pandas DataFrame for use in model
            request_data.update((x,[y]) for x,y in request_data.items())
            df = pd.DataFrame.from_dict(request_data)

            # Performing the manual equivalent of one-hot encoding for the top 20 most popular amenities.
            df['Wifi'] = df['amenities'].str.contains('Wifi')
            df['Kitchen'] = df['amenities'].str.contains('Kitchen')
            df['Heating'] = df['amenities'].str.contains('Heating')
            df['Essentials'] = df['amenities'].str.contains('Essentials')
            df['Hair dryer'] = df['amenities'].str.contains('Hair dryer')
            df['Laptop friendly workspace'] = df['amenities'].str.contains('Laptop friendly workspace')
            df['Hangers'] = df['amenities'].str.contains('Hangers')
            df['Iron'] = df['amenities'].str.contains('Iron')
            df['Shampoo'] = df['amenities'].str.contains('Shampoo')
            df['TV'] = df['amenities'].str.contains('TV')
            df['Hot water'] = df['amenities'].str.contains('Hot water')
            df['Internet'] = df['amenities'].str.contains('Internet')
            df['Host greets you'] = df['amenities'].str.contains('Host greets you')
            df['Smoke detector'] = df['amenities'].str.contains('Smoke detector')
            df['Buzzer/wireless intercom'] = df['amenities'].str.contains('Buzzer/wireless intercom')
            df['Lock on bedroom door'] = df['amenities'].str.contains('Lock on bedroom door')
            df['Buzzer/wireless intercom'] = df['amenities'].str.contains('Buzzer/wireless intercom')
            df['Refrigerator'] = df['amenities'].str.contains('Refrigerator')
            df['Free street parking'] = df['amenities'].str.contains('Free street parking')
            df['Dishes and silverware'] = df['amenities'].str.contains('Dishes and silverware')
            df = df.drop(columns='amenities')

            # creating dataframe variable from dictionary
            ##Alternative to method above. Ran into errors 
            #df = pd.DataFrame.from_dict(x, orient='index').transpose()

            # Make prediction based on created dataframe of user input data
            result = model.predict(df)

            #Creating dict to convert to json and return
            output = {'result': int(result[0])}

            return jsonify(results=output)

        except Exception as e:
            return jsonify({'Error': e})

    else:
        return jsonify({'Error': 'No Model Available'})

if __name__ == '__main__':
    app.run(debug=True)
