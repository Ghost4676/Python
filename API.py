import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
 
# data = response.json()["timestamp"]
# print(data)

####################################################

MY_LAT = 51.587351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
}

## Actual URL Requirements
## https://api.sunrise-sunset.org/json&lat=10&lon=98
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)
print(data["results"]["sunrise"])