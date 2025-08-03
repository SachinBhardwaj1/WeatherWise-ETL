import os
from utils.api import fetch_openmeteo_weather
from utils.transform import transform_openmeteo_data

def run_pipeline(lat, lon, start_date, end_date, output_path):
    raw = fetch_openmeteo_weather(lat, lon, start_date, end_date)
    df = transform_openmeteo_data(raw)
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")