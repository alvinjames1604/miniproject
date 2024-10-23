from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd  # Import pandas
import xgboost as xgb

app = Flask(__name__)

# Load the pre-trained XGBRegressor model
loaded_model = xgb.XGBRegressor()
loaded_model.load_model('xgb_regressor.model')  # Adjust the path to your model file

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()
        
        # Extract features from the received JSON data
        gender = 1 if data['gender'] == 'male' else 0
        age = data['age']
        height = data['height']
        weight = data['weight']
        duration = data['duration']
        heartRate = data['heartRate']
        bodyTemp = data['bodyTemp']
        
        # Create a DataFrame for the model
        features = pd.DataFrame({
            "Gender": [gender],
            "Age": [age],
            "Height": [height],
            "Weight": [weight],
            "Duration": [duration],
            "Heart_Rate": [heartRate],
            "Body_Temp": [bodyTemp],
        })
        
        print(features)  # Optional: For debugging purposes
        
        # Make the prediction
        prediction = loaded_model.predict(features)
        
        print(prediction)
        
        # Convert prediction to float
        calories_burnt = float(prediction[0])  # Convert to Python float
        
        # Return the result as JSON
        return jsonify({'calories_burnt': calories_burnt})
    
    except Exception as e:
        # Return an error message in case of an exception
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
