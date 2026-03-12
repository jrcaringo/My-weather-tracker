# import streamlit as st
# import requests

# API_KEY = "33db7e90fab4e248bd60a129ffc66eee"

# st.title("Weather Tracker")

# city = st.text_input("Enter city")

# if city:
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
#     data = response.json()

#     if data["cod"] == 200:
#         temp = data["main"]["temp"]
#         humidity = data["main"]["humidity"]
#         weather = data["weather"][0]["description"]

#         st.write(f"Temperature: {temp}°C")
#         st.write(f"Humidity: {humidity}%")
#         st.write(f"Condition: {weather}")
#     else:
#         st.write("City not found.")

import streamlit as st
import requests
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEY"

# Page title
st.title("🌤 Live Weather Tracker")

st.markdown("### Real-Time Weather Dashboard")

city = st.text_input("Enter city")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        st.subheader(f"Weather in {city}")

        col1, col2, col3 = st.columns(3)

        col1.metric("Temperature 🌡", f"{temp} °C")
        col2.metric("Humidity 💧", f"{humidity} %")
        col3.metric("Condition ☁", weather.title())

        # ----- Matplotlib Chart -----
        labels = ["Temperature (°C)", "Humidity (%)"]
        values = [temp, humidity]

        fig, ax = plt.subplots()
        bars = ax.bar(labels, values, color=["orange", "skyblue"])

        ax.set_title("Weather Metrics Visualization")
        ax.set_ylabel("Values")

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 0.5,
                    f"{height}", ha='center')

        st.pyplot(fig)

    else:
        st.error("City not found.")

# Footer / Project Credit
st.markdown("---")
st.markdown(
    "👨‍💻 **Project by James Ryan Aringo**  \n"
    "Python Weather Dashboard using OpenWeather API, Streamlit, and Matplotlib."
)