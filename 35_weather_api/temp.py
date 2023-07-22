import requests

api_key = '3628061ff3dc861da0168f2b51b3450abbb'

owm_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
paramss = {
    'lat':-20.316839,
    'lon':-40.309921,
    'appid':api_key
}

response = requests.get(owm_endpoint,params=paramss)
print(response.json())