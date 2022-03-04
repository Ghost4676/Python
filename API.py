import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
 
# data = response.json()["timestamp"]
# print(data)

####################################################

# MY_LAT = 51.587351
# MY_LONG = -0.127758

# parameters = {
#     "lat": MY_LAT,
#     "lon": MY_LONG,
# }

# ## Actual URL Requirements
# ## https://api.sunrise-sunset.org/json&lat=10&lon=98
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# #print(data)
# print(data["results"]["sunrise"])

###################################################

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "453453464634634jk6j34k6j3k4"

weather_params = {
    "lat": 51.5464,
    "lon": -56.555,
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
print(response.json())
weather_data = response.json()
weather_slice = weather_data["hourly"][:11]   # data from 0-11

will_rain = False
for hour_data in weather_slice:
    print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella")
        will_rain = True

if will_rain:
    print("Bring an umbrella")

# print(weather_data["hourly"][0]["weather"][0]["id"])
