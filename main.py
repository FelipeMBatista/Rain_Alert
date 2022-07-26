import requests
from twilio.rest import Client
import os

API_KEY = os.environ["TWILIO_API_KEY"]
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

parameters = {
    "lat": -29.446730,
    "lon": -50.579762,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

# weather_id = [data["hourly"][count]["weather"][0]["id"] for count in range(0,12)]
# for id in weather_id:
#     if id < 700:
#         print("hello")

#Using Slice to create a list
will_rain = False
weather_slice = data["hourly"][:12]
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="BOM DIA MEU AMOOOOOOOOR ❤ hoje vai chover! Não esqueça o guarda chuva! ☔. Te amo, beijos.",
        from_='+13392184603',
        to='+5554999558127'
    )
    print(message.status)