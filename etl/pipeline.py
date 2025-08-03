import os
from utils.api import fetch_weather_data
from utils.transform import transform_weather_data

def run_pipeline(api_key, lat, lon, output_path):
    raw = fetch_weather_data(api_key, lat, lon)
    df = transform_weather_data(raw)
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")