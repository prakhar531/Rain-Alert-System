import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "d136e03a15dda7e75b2dc765a04ad1cd"

account_sid = "AC3472c7accde44b2293b00b1aec451415"
auth_token = "2876dc9326d291f6a8320e5026d1dd88"

weather_params = {
    "lat": "55.864239",
    "lon": "-4.251806",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(response.json())
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = True

for hour_data in weather_slice:

    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("It will rain")

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It,s going to rain🌧️today.Please carry your umbralla☂️",
        from_="+19205411931",
        to="+91 97092 98279"
    )
    print(message.status)
