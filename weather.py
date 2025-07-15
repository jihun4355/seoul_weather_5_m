
import requests
import csv
import os
from datetime import datetime
API_KEY = os.getenv("API_KET_W")
city = "seoul"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
result= response.json()
temp = result["main"]["temp"]
humidity = result["main"]["humidity"]
weather = result["weather"][0]["main"]
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



header = ["current_time", "weather", "temp", "humidity"]

csv_exist = os.path.exists("seoul_weather.csv")


with open("seoul_weather.csv", "a") as file:
    writer = csv.writer(file)

    if not csv_exist:
        writer.writerow(header)
    writer.writerow([current_time, weather, temp, humidity])
    print("서울 기온 저장 완료")
