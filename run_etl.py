from etl.pipeline import run_pipeline

API_KEY = 'openweather_api_key'
LAT = 34.0489
LON = 111.0937
OUTPUT = 'data/weatherData.csv'

if __name__ == '__main__':
    run_pipeline(API_KEY, LAT, LON, OUTPUT)