import requests
from datetime import datetime

KEY = '733075e09b3b08f03708291db53f9949'
APP_ID = '49198fe7'

# my data
GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 179
AGE = 30

headers = {
    'x-app-id':APP_ID,
    'x-app-key':KEY,
    # 'x-remote-user-id':'0'
}
exercise_text = input("What exercise I did?")

parameters = {
    "query":exercise_text,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
}

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint = 'https://api.sheety.co/f3470e211834f548b9ce078ad88251ff/myWorkoutsPython/workouts'

response = requests.post(exercise_endpoint,json=parameters,headers=headers)

result = response.json()

print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    #Bearer Token Authentication
    bearer_headers = {
    "Authorization": "Bearer AZDSXSDCDFVF"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers
    )

    print(sheet_response.text)
