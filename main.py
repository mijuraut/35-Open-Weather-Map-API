import requests

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "936861fbc39ce1f6bb0e1cea570af802"

# ?lat={61.058449}&lon={28.186991}&appid=936861fbc39ce1f6bb0e1cea570af802

weather_params = {
    "lat": 61.058449,
    "lon": 28.186991,
    "appid": api_key
}

response = requests.get(OMW_Endpoint, params=weather_params)
# response.raise_for_status()
print(response.status_code)

# data = response.json()
# weather_data = data["results"]

# print(weather_data)

# One Call API

# Lappeenranta:
# lat = 61.058449
# lng = 28.186991