#!/usr/bin/python3

from pyowm.owm import OWM
from datetime import datetime


owm = OWM('****************888') 
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Tel Aviv,IL')
weather = observation.weather

# 1. Get the current weather in Tel Aviv. 
print(weather.detailed_status)
print(weather.temperature('celsius')['temp'])


# 2. Get current wind info of Tel Aviv.
print(weather.wind())


#3. Get today’s sunrise and sunset times of Tel Aviv.
print(weather.sunrise_time())
print(weather.sunset_time())

#4. Display all these information in a user friendly way.
print("Weather:", weather.detailed_status)
print("Temperature:", weather.temperature('celsius')['temp'])
print("Wind:", weather.wind())
sunrise = datetime.utcfromtimestamp(weather.sunrise_time()).strftime('%H:%M:%S')
sunset = datetime.utcfromtimestamp(weather.sunset_time()).strftime('%H:%M:%S')
print("Sunrise:", sunrise)
print("Sunset:", sunset)


#5. Recreate these steps, but this time, ask the user for a location (display the information in a user friendly way).
#
#    Instead of working with the name of the city, retrieve the id of the city.
#    Check out the documentation section : “Identifying cities and places via city IDs”.

city_id = 293918  # Netanya
observation = mgr.weather_at_id(city_id)
weather = observation.weather
city_name = observation.location.name
print(f"City: {city_name}")

print("Weather:", weather.detailed_status)
print("Temperature:", weather.temperature('celsius')['temp'])
print("Wind:", weather.wind())
sunrise = datetime.utcfromtimestamp(weather.sunrise_time()).strftime('%H:%M:%S')
sunset = datetime.utcfromtimestamp(weather.sunset_time()).strftime('%H:%M:%S')
print("Sunrise:", sunrise)
print("Sunset:", sunset)


#Retrieve weather forecasts : The OpenWeatherMap free tier gives you access to 5 day forecasts. The forecasts contain the weather data in three-hour intervals.

#    The methods for retrieving the forecast are:
#        forecast_at_place('Los Angeles, US', '3h')
#        forecast_at_id(5391959, '3h')
#        forecast_at_coords(lat=37.774929, lon=-122.419418, interval='3h')
#        Forecasts are useful if you want to know what the weather conditions will be throughout the day/week.

forecast = mgr.forecast_at_id(city_id, '3h')
weathers = forecast.forecast.weathers
print(f"Netanya (next {len(weathers)} periods of 3h) ---")
for weather in weathers:
    time = datetime.fromtimestamp(weather.reference_time())
    temp = weather.temperature('celsius')['temp']
    status = weather.detailed_status
    humidity = weather.humidity
    print(f"{time.strftime('%d/%m %H:%M')} | {status:20} | Temp: {temp}°C | Umidade: {humidity}%")


# 7. Use this API to retrieve the Air Pollution in a specific city.

location = observation.location
city_id = 293918  # Netanya
observation = mgr.weather_at_id(city_id)

lat = location.lat
lon = location.lon

air_mgr = owm.airpollution_manager()
air_data = air_mgr.air_quality_at_coords(lat, lon)

aqi = air_data.aqi
print(air_data.to_dict()['air_quality_data'])
components = air_data.to_dict()['air_quality_data']

print(f"Air Pollution in {location.name}")
print(f"AQI (Air Quality Index): {aqi} (1 = Good, 5 = Very Poor)")
print("Pollutants (μg/m³):")
for comp, value in components.items():
    print(f"  {comp.upper():<5}: {value}")
