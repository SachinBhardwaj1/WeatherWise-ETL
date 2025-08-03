import requests
import datetime

def fetch_weather_data(api_key, lat, lon, days=7):
    base_url = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
    all_data = []

    for day in range(days):
        dt = int((datetime.datetime.now() - datetime.timedelta(days=day)).timestamp())
        params = {
            'lat': lat,
            'lon': lon,
            'dt': dt,
            'appid': api_key,
            'units': 'metric'
        }
        res = requests.get(base_url, params=params)
        if res.status_code == 200:
            all_data.append(res.json())
        else:
            print(f"Failed to fetch data for {dt}")
    return all_data