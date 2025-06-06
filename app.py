import streamlit as st


#'''
# TaxiFareModel front
#'''

#st.markdown('''
#Remember that there are several ways to output content into your web page...

#Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
#''')

#'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

#1. Let's ask for:
#- date and time
#- pickup longitude
#- pickup latitude
#- dropoff longitude
#- dropoff latitude
#- passenger count
#'''

import datetime

st.title("🗽 NYC Taxi Fare Prediction")

st.markdown('''
Enter your trip details below, then click *Predict fare* to see the estimated taxi fare.
''')

# Date and time input
date = st.date_input("Pickup date", datetime.date.today())
time = st.time_input("Pickup time", datetime.datetime.now().time())

# Coordinates input
pickup_long = st.number_input("Pickup Longitude", value=-73.985428)
pickup_lat = st.number_input("Pickup Latitude", value=40.748817)
dropoff_long = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_lat = st.number_input("Dropoff Latitude", value=40.748817)

# Passenger count
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

pickup_datetime = f"{date} {time}"




#'''
## Once we have these, let's call our API in order to retrieve a prediction

#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

#🤔 How could we call our API ? Off course... The `requests` package 💡
#'''

url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

    #st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

#'''

#2. Let's build a dictionary containing the parameters for our API...

#3. Let's call our API using the `requests` package...

#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
#'''

# Build the Parameters Dictionary
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_long,
    "pickup_latitude": pickup_lat,
    "dropoff_longitude": dropoff_long,
    "dropoff_latitude": dropoff_lat,
    "passenger_count": passenger_count
}


# Call the API with requests
import requests

'''
#### 🚖🔮💰 Ready to ride?
'''


if st.button("Predict fare"):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json().get("fare", "No fare returned")
        st.success(f"🚕 Predicted Fare: ${round(prediction, 2)}")
    else:
        st.error("❌ Error with the API call. Check your parameters or try again later.")



import pandas as pd

map_data = pd.DataFrame({
    'lat': [pickup_lat, dropoff_lat],
    'lon': [pickup_long, dropoff_long]
})

st.map(map_data)
