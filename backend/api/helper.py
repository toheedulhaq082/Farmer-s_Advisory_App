import pip._vendor.requests as requests
from datetime import datetime, timedelta
from .models import Weather 
import numpy as np
import pandas as pd
import joblib
import os   
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')

def fetch_weather_data(city):
    api_key = API_KEY
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={city}'
    response = requests.get(url)
    return response.json()

# def get_weather_image(description):
#     images = {
#         'Clear': '../backend/media/images/clear.png',
#         'Partly Cloudy': '../backend/media/images/Partlycloudy2.png',
#         'Cloudy': '../backend/media/images/cloudy.png',
#         'Overcast': '../backend/media/images/cloudy.png',
#         'Fog': '../backend/media/images/mist.png',
#         'Haze': '../backend/media/images/mist.png',
#         'Mist': '../backend/media/images/mist.png',
#         'Rain': '../backend/media/images/Rain.png',
#         'Drizzle': '../backend/media/images/Rain.png',
#         'Showers': '../backend/media/images/Rain.png',
#         'Thunderstorm': '../backend/media/images/Thunderstorm.png',
#         'Snow': '../backend/media/images/Snow.png',
#         'Sleet': '../backend/media/images/Snow.png',
#         'Hail': '../backend/media/images/Snow.png',
#         'Windy': '../backend/media/images/Windy.png',
#         'Blizzard': '../backend/media/images/Snow.png',
#         'Tornado': '../backend/media/images/Tornado.png',
#     }

#     return images.get(description, '../backend/media/images/default.png')


def store_weather_data(data, predictions):

    int_predictions = [int(pred) for pred in predictions]

    if 'current' in data and 'location' in data:

        current_date = datetime.strptime(data['location']['localtime'], "%Y-%m-%d %H:%M").date()
        
        day_names = [(current_date + timedelta(days=i)).strftime('%a') for i in range(1, 8)]

        weather = Weather(
            city=data['location']['name'],
            country=data['location']['country'],
            date=datetime.strptime(data['location']['localtime'], "%Y-%m-%d %H:%M").date(),
            temp=data['current']['temperature'],
            temp_feels_like=data['current']['feelslike'],
            precipitation=data['current']['precip'],
            pressure=data['current']['pressure'],
            humidity=data['current']['humidity'],
            description=data['current']['weather_descriptions'][0],
            wind_speed=data['current']['wind_speed'],
            wind_deg=data['current']['wind_degree'],
            wind_dir=data['current']['wind_dir'],
            timezone=int(float(data['location']['utc_offset'])),
            # image_path=get_weather_image(data['current']['weather_descriptions'][0]),
            day_1_name=day_names[0],
            day_2_name=day_names[1],
            day_3_name=day_names[2],
            day_4_name=day_names[3],
            day_5_name=day_names[4],
            day_6_name=day_names[5],
            day_7_name=day_names[6],
            
            day_0_temp=int_predictions[0],
            day_1_temp=int_predictions[1],  # Predictions are indexed from 0 to 6 for the 7 days
            day_2_temp=int_predictions[2],
            day_3_temp=int_predictions[3],
            day_4_temp=int_predictions[4],
            day_5_temp=int_predictions[5],
            day_6_temp=int_predictions[6],
            day_7_temp=int_predictions[7]
        )
        weather.save()
    else:
        print("Error: Couldn't fetch the weather data. Please check the API response.")


def getPrediction(city):
    print(city)
    data = fetch_weather_data(city)

    if city == 'Multan':
        print('prediction for Multan')
        # Input variables: T_max, T_avg, T_min, RH_max, RH_min, RH_avg, WS_max, WS_avg, WS_min, es-ea, Rs, Rn, Julian_Day
        input_data = np.array([[20.55555556, 14.30555556, 8.888888889, 94, 60, 78.62, 2.2352, 0.78232, 0, 0.518167193, 13.25569494, 6.316949165, 38]])
        
        scaler = joblib.load('models/Multan/scaler.pkl')
        input_scaled = scaler.transform(input_data)
        
        predictions = []
        
        model_names = ['model_ETo.pkl', 'model_Lead_1.pkl', 'model_Lead_2.pkl',
                       'model_Lead_3.pkl', 'model_Lead_4.pkl', 'model_Lead_5.pkl',
                       'model_Lead_6.pkl', 'model_Lead_7.pkl']
        
        current_input = input_scaled
    
        model = joblib.load(f'models/Multan/{model_names[0]}')
        eto_prediction = model.predict(current_input)
        predictions.append(eto_prediction)
        
        print(f"ETo Prediction: {eto_prediction[0]}")
        
        for i in range(1, len(model_names)):
            current_input = np.hstack([current_input, predictions[-1].reshape(-1, 1)])
            
            model = joblib.load(f'models/Multan/{model_names[i]}')
            lead_prediction = model.predict(current_input)
            predictions.append(lead_prediction)
            
            print(f"Lead {i} Prediction: {lead_prediction[0]}")
        
        
        store_weather_data(data, predictions)

    elif city == 'Hyderabad':
        print('prediction for Hyderabad')
        # Input variables: T_max, T_avg, T_min, RH_max, RH_min, RH_avg, WS_max, WS_avg, WS_min, es-ea, Rs, Rn, Julian_Day
        input_data = np.array([[20.55555556, 14.30555556, 8.888888889, 94, 60, 78.62, 2.2352, 0.78232, 0, 0.518167193, 13.25569494, 6.316949165, 38]])
        
        scaler = joblib.load('models/hyderabad/scaler.pkl')
        input_scaled = scaler.transform(input_data)
        
        predictions = []
        
        model_names = ['model_ETo.pkl', 'model_Lead_1.pkl', 'model_Lead_2.pkl',
                       'model_Lead_3.pkl', 'model_Lead_4.pkl', 'model_Lead_5.pkl',
                       'model_Lead_6.pkl', 'model_Lead_7.pkl']
        
        current_input = input_scaled
    
        model = joblib.load(f'models/hyderabad/{model_names[0]}')
        eto_prediction = model.predict(current_input)
        predictions.append(eto_prediction)
        
        print(f"ETo Prediction: {eto_prediction[0]}")
        
        for i in range(1, len(model_names)):
            current_input = np.hstack([current_input, predictions[-1].reshape(-1, 1)])
            
            model = joblib.load(f'models/hyderabad/{model_names[i]}')
            lead_prediction = model.predict(current_input)
            predictions.append(lead_prediction)
            
            print(f"Lead {i} Prediction: {lead_prediction[0]}")
        
        print(data, predictions)
        store_weather_data(data, predictions)

        
    elif city == 'Bahawalpur':
        print('prediction for bahawalpur')
        # Input variables: T_max, T_avg, T_min, RH_max, RH_min, RH_avg, WS_max, WS_avg, WS_min, es-ea, Rs, Rn, Julian_Day
        input_data = np.array([[20.55555556, 14.30555556, 8.888888889, 94, 60, 78.62, 2.2352, 0.78232, 0, 0.518167193, 13.25569494, 6.316949165, 38]])
        
        scaler = joblib.load('models/Bahawalpur/scaler.pkl')
        input_scaled = scaler.transform(input_data)
        
        predictions = []
        
        model_names = ['model_ETo.pkl', 'model_Lead_1.pkl', 'model_Lead_2.pkl',
                       'model_Lead_3.pkl', 'model_Lead_4.pkl', 'model_Lead_5.pkl',
                       'model_Lead_6.pkl', 'model_Lead_7.pkl']
        
        current_input = input_scaled
    
        model = joblib.load(f'models/Bahawalpur/{model_names[0]}')
        eto_prediction = model.predict(current_input)
        predictions.append(eto_prediction)
        
        print(f"ETo Prediction: {eto_prediction[0]}")
        
        for i in range(1, len(model_names)):
            current_input = np.hstack([current_input, predictions[-1].reshape(-1, 1)])
            
            model = joblib.load(f'models/Bahawalpur/{model_names[i]}')
            lead_prediction = model.predict(current_input)
            predictions.append(lead_prediction)
            
            print(f"Lead {i} Prediction: {lead_prediction[0]}")

        print(data, predictions)
        store_weather_data(data, predictions)


def filter_current_month(data):
    # Get the current month (1 = January, 12 = December)
    current_month = datetime.now().month
    
    # Map of month indices to month names
    month_names = {
        1: "jan", 2: "feb", 3: "mar", 4: "apr", 5: "may", 6: "jun",
        7: "jul", 8: "aug", 9: "sep", 10: "oct", 11: "nov", 12: "dec"
    }
    
    # Get the current month name
    current_month_name = month_names[current_month]
    
    # Extract the relevant data for the current month
    filtered_data = []
    for entry in data:
        crop_info = entry.get('crop', {})
        province_info = entry.get('province', None)
        current_month_value = entry.get(current_month_name, None)
        
        filtered_entry = {
            'crop': crop_info,
            'province': province_info,
            current_month_name: current_month_value
        }
        
        filtered_data.append(filtered_entry)
    
    return filtered_data

def get_day_temp(weather_data, day_number):
    # Check if the number is within the valid range
    if day_number < 1 or day_number > 7:
        return "Invalid number. Please enter a number between 1 and 7."
    
    # Dynamically access the day_temp based on the day_number
    day_temp_key = f"day_{day_number - 1}_temp"
    
    # Get the corresponding day_temp from the weather_data
    day_temp = weather_data.get(day_temp_key)
    
    if day_temp is not None:
        return day_temp
    else:
        return f"{day_temp_key} not found in weather_data."