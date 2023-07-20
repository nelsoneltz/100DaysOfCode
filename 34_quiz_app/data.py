import requests

parameters = {
    'amount':10,
    'type':'boolean'
}
endpoint = 'https://opentdb.com/api.php'

response = requests.get(endpoint,params=parameters,verify=False)
response.raise_for_status()
data = response.json()



question_data = data['results']