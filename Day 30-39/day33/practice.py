import requests
from datetime import datetime

MY_LAT = 8.980603
MY_LONG = 38.757759
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
data = response.json()

time_now = datetime.now()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(time_now.hour)