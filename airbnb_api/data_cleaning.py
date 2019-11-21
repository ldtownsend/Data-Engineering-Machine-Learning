"""
Contains wrangle function to create boolean columns for common amenities
"""

import pandas as pd


def wrangle(df):
    """
    Takes the dataframe created in app.py and creates boolean columns
    for most common amenities
    """
    # List of most frequent amenities
    top_amenities_list = ['Wifi', 'Kitchen', 'Heating', 'Essentials',
                          'Hairdryer', 'Laptopfriendlyworkspace',
                          'Hangers', 'Iron', 'Shampoo', 'TV', 'Hotwater',
                          'Internet', 'Hostgreetsyou', 'Smokedetector',
                          'Buzzer/wirelessintercom', 'Lockonbedroomdoor',
                          'Refrigerator', 'Freestreetparking',
                          'Dishesandsilverware']
    # Copying dataframe to prevent errors
    # df = df.copy()

    # loop to create Boolean columns for each amenity
    for amenity in top_amenities_list:
        df[amenity] = df['amenities'].str.contains(amenity)

    # Dropping column that contained all amenities
    df = df.drop(columns='amenities')

    return df
