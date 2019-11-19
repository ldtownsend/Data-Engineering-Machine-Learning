'''Example app.py file. TODO - '''
from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle

# app
app = Flask(__name__)

# where the pickled models would go if we choose to pickle
# pickle.dump(model, open(‘model.pkl’, ‘wb’))

# routes
@app.route('/', methods=['GET','POST'])
def root():
    """
    Base for directory. Will return base.html template
    """
    header = 'Welcome!'
    return render_template('base.html', message=header)

@app.route('/request', methods=[]'GET','POST'])
def fetch_data():
    """
    Fetches data in a JSON format to be fed into predictive model
    """


if __name__ == '__main__':
    app.run(debug=True)
