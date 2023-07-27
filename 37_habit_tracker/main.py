import requests
from datetime import datetime



TOKEN = "AZASXSDCD"
USERNAME = 'user1nf'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token':TOKEN,
    "username":USERNAME,
    "agreeTermsofService":"yes",
    "notMinor":"yes",
}


# response = requests.post(pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    'id':'graph1',
    "name":"Pages Read",
    "unit":"Pages",
    "type":"int",
    "color":"momiji"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

add_pixel_params = {
    # 'date': datetime.today().strftime('%Y%m%d'),
    'date':'20230724', 
    "quantity":'15'
}

add_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_params["id"]}'

# response = requests.post(url=add_pixel_endpoint,json=add_pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f'{add_pixel_endpoint}/20230724'

update_params = {
    'quantity':"50"
}

response = requests.put(url=update_pixel_endpoint,json=update_params,headers=headers)
print(response.text)
