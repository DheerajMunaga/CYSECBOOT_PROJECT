import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
m="\n-------------------------------------------------------------\n"

r=open('textfile1.txt','w')
a=(m)
b=("Weather Stats for - {}  || {}".format(location.upper(), date_time))
c=(m)
d=("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
e=("\nCurrent weather desc  : {}".format(weather_desc))
f=("\nCurrent Humidity      : {} %".format(hmdt))
g=("\nCurrent wind speed    : {}kmph ".format(wind_spd))
r.write(a)
r.write(b)
r.write(c)
r.write(d)
r.write(e)
r.write(f)
r.write(g)
r.close()

