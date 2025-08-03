import datetime
import pandas as pd

def transform_weather_data(raw_data):
    daily_data = []
    for day_data in raw_data:
        temps = [h['temp'] for h in day_data.get('hourly', [])]
        hums = [h['humidity'] for h in day_data.get('hourly', [])]
        if temps and hums:
            avg_temp = sum(temps) / len(temps)
            avg_humidity = sum(hums) / len(hums)
            date = datetime.datetime.fromtimestamp(day_data['current']['dt']).strftime('%Y-%m-%d')
            daily_data.append({'date': date, 'avg_temp': avg_temp, 'avg_humidity': avg_humidity})
    return pd.DataFrame(daily_data)