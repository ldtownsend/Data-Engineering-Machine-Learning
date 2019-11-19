'''Example app.py file. TODO - '''
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle


# app
app = Flask(__name__)

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
            data_df = pd.DataFrame.from_dict(request_data)

            # Make prediction based on created dataframe of user input data
            result = model.predict(data_df)

            #Creating dict to convert to json and return
            output = {'result': int(result[0])}

            return jsonify(results=output)

        except Exception as e:
            return jsonify({'Error': e})

    else:
        return jsonify({'Error': 'No Model Available'})

if __name__ == '__main__':
    app.run(debug=True)
