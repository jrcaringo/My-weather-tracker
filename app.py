# # import necessary libraries
# import requests

# # define base URL
# base_url = "http://api.openweathermap.org/data/2.5/forecast"

# # define parameters
# parameters = {"q": "Paris,FR", "appid": "33db7e90fab4e248bd60a129ffc66eee"}

# # make API request, passing in base URL and parameters
# response = requests.get(base_url, params = parameters)

# # print out text from API response
# print(response.text)

# import requests

# API_KEY = "33db7e90fab4e248bd60a129ffc66eee"
# city = "Manila"

# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# response = requests.get(url)
# data = response.json()

# temp = data["main"]["temp"]
# humidity = data["main"]["humidity"]
# weather = data["weather"][0]["description"]

# print(f"City: {city}")
# print(f"Temperature: {temp}°C")
# print(f"Humidity: {humidity}%")
# print(f"Condition: {weather}")

import streamlit as st
import requests

API_KEY = "33db7e90fab4e248bd60a129ffc66eee"

st.title("Weather Tracker")

city = st.text_input("Enter city")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        st.write(f"Temperature: {temp}°C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Condition: {weather}")
    else:
        st.write("City not found.")