import requests

def fetch_openmeteo_weather(lat, lon, start_date, end_date):
    base_url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        'latitude': lat,
        'longitude': lon,
        'start_date': start_date,
        'end_date': end_date,
        'timezone': 'America/Phoenix',
        'daily': (
            'temperature_2m_max,temperature_2m_min,'
            'relative_humidity_2m_max,relative_humidity_2m_min,'
            'precipitation_sum'
        )
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

