import psycopg2
import logging
import joblib
from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Display the current working directory for debugging
cwd = os.getcwd()
print("Current working directory:", cwd)

# Load the ML model using a relative path
model_path = os.path.join(cwd, 'Webapp', 'static', 'random_forest_model.joblib')
try:
    model = joblib.load(model_path)
    print("Model loaded successfully.")
except FileNotFoundError as e:
    print(f"File not found: {e}")
    print(f"Tried to load model from: {model_path}")
except Exception as e:
    print(f"Error loading model: {e}")

# Set the log level to DEBUG to capture all types of log messages
app.logger.setLevel(logging.DEBUG)

# Setup file handler for logging
log_path = os.path.join(cwd, 'Webapp', 'static', 'log', 'app.log')
file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.DEBUG)

# Optionally, you can set a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the app logger
app.logger.addHandler(file_handler)

########################################################################################################################################################
#def predict_property_value(inputs):
#
#    app.logger.debug("Debug individual inputs:")
#    app.logger.debug("Living Sqft Input: %s", inputs.get('livingsquareftInput', 'Not Found'))
#    app.logger.debug("Lot Sqft Input: %s", inputs.get('squareFootageInput', 'Not Found'))
#
#    feature_order = [
#        'living_area_sqft', 'lot_sqft', 'number_of_rooms', 'beds', 'total_baths', 
#        'has_basement', 'has_garage', 'county_Alamance', 'county_Caswell', 'county_Chatham', 
#        'county_Cumberland', 'county_Durham', 'county_Edgecombe', 'county_Franklin', 
#        'county_Gaston', 'county_Graham', 'county_Granville', 'county_Guilford', 
#        'county_Halifax', 'county_Harnett', 'county_Johnston', 'county_Jones', 
#        'county_Kerr Lake', 'county_Lee', 'county_Moore', 'county_Nash', 'county_Orange', 
#        'county_Person', 'county_Randolph', 'county_Sampson', 'county_Vance', 'county_Wake', 
#        'county_Warren', 'county_Wayne', 'county_Wilkes', 'county_Wilson'
#    ]
#
#    # Initialize the features with default values
#    features = {feature: 0 for feature in feature_order}
#
#    # Extract and convert each feature from the inputs
#    # The keys should exactly match those in the HTML form
#    features['living_area_sqft'] = float(inputs.get('livingsquareftInput', 0))
#    features['lot_sqft'] = float(inputs.get('squareFootageInput', 0))
#    features['number_of_rooms'] = int(inputs.get('roomSelect', 0))
#    features['beds'] = int(inputs.get('bedroomSelect', 0))
#    features['total_baths'] = float(inputs.get('bathroomSelect', 0))
#    features['has_basement'] = 1 if inputs.get('basementSelect', 'False') == 'True' else 0
#    features['has_garage'] = 1 if inputs.get('garageSelect', 'False') == 'True' else 0
#
#
#    # Handling county input
#    county_input = inputs.get('countyInput', '')
#    if f'county_{county_input}' in features:
#        features[f'county_{county_input}'] = 1
#
#    # Prepare data for model prediction
#    app.logger.debug("Final features for model: %s", features)
#
#    model_input = pd.DataFrame([features], columns=feature_order)
#    prediction = model.predict(model_input)
#    return prediction[0]
#
######################################################################################################################################################## 
def get_counties():
    try:
        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
        cur = conn.cursor()
        query = "SELECT DISTINCT county FROM real_estate ORDER BY county"
        print("Executing query:", query)  # Debug: print the SQL query
        cur.execute(query)
        counties = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return counties
    except psycopg2.Error as e:
        print("Error fetching counties:", e)
        return []

######################################################################################################################################################## 
def get_bathrooms():
    try:
        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
        cur = conn.cursor()
        query = "SELECT DISTINCT total_baths FROM real_estate ORDER BY total_baths"
        print("Executing query:", query)  # Debug: print the SQL query
        cur.execute(query)
        bathrooms = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return bathrooms
    except psycopg2.Error as e:
        print("Error fetching bathrooms:", e)
        return []    
    
######################################################################################################################################################## 
def get_bedrooms():
    try:
        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
        cur = conn.cursor()
        query = "SELECT DISTINCT beds FROM real_estate ORDER BY beds"
        print("Executing query:", query)  # Debug: print the SQL query
        cur.execute(query)
        bedrooms = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return bedrooms
    except psycopg2.Error as e:
        print("Error fetching bedrooms:", e)
        return [] 
      
######################################################################################################################################################## 
#def get_cities():  
#    try:
#        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
#        cur = conn.cursor()
#        query = "SELECT DISTINCT city FROM real_estate ORDER BY city"
#        print("Executing query:", query)  # Debug: print the SQL query
#        cur.execute(query)
#        cities = [row[0] for row in cur.fetchall()]
#        cur.close()
#        conn.close()
#        return cities
#    except psycopg2.Error as e:
#        print("Error fetching cities:", e)
#        return []
#
######################################################################################################################################################## 
def get_garages():
    try:
        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
        cur = conn.cursor()
        query = "SELECT DISTINCT has_garage FROM real_estate"
        print("Executing query:", query)  # Debug: print the SQL query
        cur.execute(query)
        garages = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return garages
    except psycopg2.Error as e:
        print("Error fetching garages:", e)
        return []
    
######################################################################################################################################################## 
def get_basements():
    try:
        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
        cur = conn.cursor()
        query = "SELECT DISTINCT has_basement FROM real_estate"
        print("Executing query:", query)  # Debug: print the SQL query
        cur.execute(query)
        basements = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return basements
    except psycopg2.Error as e:
        print("Error fetching basements:", e)
        return []   

######################################################################################################################################################## 
#def get_waterfronts():
#    try:
#        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
#        cur = conn.cursor()
#        query = "SELECT DISTINCT is_waterfront FROM real_estate"
#        print("Executing query:", query)  # Debug: print the SQL query
#        cur.execute(query)
#        waterfronts = [row[0] for row in cur.fetchall()]
#        cur.close()
#        conn.close()
#        return waterfronts
#    except psycopg2.Error as e:
#        print("Error fetching waterfronts:", e)
#        return []        
#
######################################################################################################################################################## 
def get_builts():
    try:
        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
        cur = conn.cursor()
        query = "SELECT DISTINCT age_of_house FROM real_estate ORDER BY age_of_house"
        print("Executing query:", query)  # Debug: print the SQL query
        cur.execute(query)
        builts = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return builts
    except psycopg2.Error as e:
        print("Error fetching waterfronts:", e)
        return []  
    
 ######################################################################################################################################################## 
def get_rooms():
    try:
        conn = psycopg2.connect("dbname='Real_Estate' user='postgres' host='192.168.50.231' password='D0ntD01t!'")
        cur = conn.cursor()
        query = "SELECT DISTINCT number_of_rooms FROM real_estate ORDER BY number_of_rooms"
        print("Executing query:", query)  # Debug: print the SQL query
        cur.execute(query)
        rooms = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
        return rooms
    except psycopg2.Error as e:
        print("Error fetching rooms:", e)
        return [] 
       
######################################################################################################################################################## 
@app.route('/')
def home():
    # Attempt to get the real IP address if behind a proxy
    if 'X-Forwarded-For' in request.headers:
        client_ip = request.headers['X-Forwarded-For'].split(',')[0]  # Taking the first IP in the list
    else:
        client_ip = request.remote_addr

    user_agent = request.headers.get('User-Agent')
    request_method = request.method
    request_path = request.path
    app.logger.debug(f'{client_ip} accessed {request_path} using {request_method} with {user_agent}')

    counties = get_counties()
    #cities = get_cities()
    garages = get_garages()
    basements = get_basements()
    bedrooms = get_bedrooms()
    bathrooms = get_bathrooms()
    #waterfronts = get_waterfronts()
    rooms = get_rooms()
    builts = get_builts()

    try:
        return render_template('index3.html', counties=counties, garages=garages, builts=builts, 
                               basements=basements, bedrooms=bedrooms, bathrooms=bathrooms, rooms=rooms)
    except Exception as e:
        app.logger.error(f'Error processing request: {e}')
        raise

########################################################################################################################################################  
@app.route('/county')
def county():
    counties = get_counties()
    print("Counties:", counties)  # Debug: print the list of counties
    return render_template('index3.html', counties=counties)

######################################################################################################################################################## 
#@app.route('/waterfront')
#def waterfront():
#    waterfronts = get_waterfronts()
#    print("Waterfronts:", waterfronts)  # Debug: print the list of counties
#    return render_template('index3.html', waterfronts=waterfronts)
#
######################################################################################################################################################## 
@app.route('/bathroom')
def bathroom():
    bathrooms = get_bathrooms()
    print("Bathrooms:", bathrooms)  # Debug: print the list of bathrooms
    return render_template('index3.html', bathrooms=bathrooms)

######################################################################################################################################################## 
@app.route('/basement')
def basement():
    basements = get_basements()
    print("Basements:", basements)  # Debug: print the list of basements
    return render_template('index3.html', basements=basements)

######################################################################################################################################################## 
#@app.route('/city')
#def city():
#    cities = get_cities()
#    print("Cities:", cities)  # Debug: print the list of cities
#    return render_template('index3.html', cities=cities)
#
######################################################################################################################################################## 
@app.route('/garage')
def garage():
    garages = get_garages()
    print("Garages:", garages)  # Debug: print the list of garages
    return render_template('index3.html', garages=garages)

######################################################################################################################################################## 
@app.route('/bedroom')
def bedroom():
    bedrooms = get_bedrooms()
    print("Bedrooms:", bedrooms)  # Debug: print the list of garages
    return render_template('index3.html', bedrooms=bedrooms)
######################################################################################################################################################## 
@app.route('/Built')
def built():
    builts = get_builts()
    print("Builts:", builts)  # Debug: print the list of garages
    return render_template('index3.html', builts=builts)

######################################################################################################################################################## 
@app.route('/Room')
def room():
    rooms = get_rooms()
    print("Rooms:", rooms)  # Debug: print the list of garages
    return render_template('index3.html', rooms=rooms)

######################################################################################################################################################## 
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()
        app.logger.debug("Form data received: %s", data)

        # Define the features based on your model's requirements
        feature_names = [  # Assuming this is the correct order and names
            'living_area_sqft', 'lot_sqft', 'number_of_rooms', 'beds', 'total_baths', 
        'has_basement', 'has_garage', 'county_Alamance', 'county_Caswell', 'county_Chatham', 
        'county_Cumberland', 'county_Durham', 'county_Edgecombe', 'county_Franklin', 
        'county_Gaston', 'county_Graham', 'county_Granville', 'county_Guilford', 
        'county_Halifax', 'county_Harnett', 'county_Johnston', 'county_Jones', 
        'county_Kerr Lake', 'county_Lee', 'county_Moore', 'county_Nash', 'county_Orange', 
        'county_Person', 'county_Randolph', 'county_Sampson', 'county_Vance', 'county_Wake', 
        'county_Warren', 'county_Wayne', 'county_Wilkes', 'county_Wilson'
        ]

        # Initialize features with default values
        features = {name: 0 for name in feature_names}

        # Map form inputs to feature values
        features['living_area_sqft'] = float(data.get('livingsquareftInput', 0))
        features['lot_sqft'] = float(data.get('squareFootageInput', 0))
        features['number_of_rooms'] = int(data.get('roomSelect', 0))
        features['beds'] = int(data.get('bedroomSelect', 0))
        features['total_baths'] = float(data.get('bathroomSelect', 0))
        features['has_basement'] = 1 if data.get('basementSelect') == 'True' else 0
        features['has_garage'] = 1 if data.get('garageSelect') == 'True' else 0

        # One-hot encode the county feature
        county_input = data.get('countyInput')
        if county_input:
            county_feature = f'county_{county_input}'
            if county_feature in features:
                features[county_feature] = 1

        app.logger.debug("Features for model: %s", features)

        model_input = pd.DataFrame([features], columns=feature_names)
        prediction = model.predict(model_input)
        app.logger.debug("Prediction result: %s", prediction)

        return jsonify({'estimatedValue': prediction[0]})
    except Exception as e:
        app.logger.error(f'Prediction error: {e}')
        return jsonify({'error': str(e)})
    
######################################################################################################################################################## 
#@app.route('/predict-test', methods=['GET'])
#def predict_test():
#   try:
#        # Simulate form data with static test values
#        test_data = {
#            'countyInput': 'Alamance',
#            'squareFootageInput': '12000',
#            'livingsquareftInput': '2500',
#            'basementSelect': 'False',
#            'garageSelect': 'False',
#            'bedroomSelect': '1',
#            'bathroomSelect': '1.0',
#            'roomSelect': '11',
#            'builtSelect': '58'
#        }
#
#        app.logger.debug("Test data: %s", test_data)
#
#        # Call the prediction function with the test data
#        prediction = predict_property_value(test_data)
#        app.logger.debug("Test prediction result: %s", prediction)
#
#        return jsonify({'testEstimatedValue': prediction})
#    except Exception as e:
#        app.logger.error(f'Prediction test error: {e}')
#        return jsonify({'error': str(e)})
#
######################################################################################################################################################## 
if __name__ == '__main__':
    app.run(host='192.168.50.231', port=5000, debug=True)

