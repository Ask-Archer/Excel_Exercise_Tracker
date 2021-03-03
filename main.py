import requests
from datetime import datetime
import os


GENDER = "female"
WEIGHT_KG = 54
HEIGHT_CM = 167
AGE = 23

APP_ID = os.environ.get("NTR_API_ID")
APP_KEY = os.environ.get("NTR_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender":GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers = headers)
result = response.json()
print(result)


sheety_post = os.environ.get("SHEETY_URL")

today = datetime.now()

date = (today.strftime("%d%m%Y"))
time = today.strftime("%X")



for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
}

sheet_response = requests.post(url=sheety_post, json=sheet_inputs)
print(sheet_response.text)
