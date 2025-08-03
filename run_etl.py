from etl.pipeline import run_pipeline

START_DATE = '1990-07-01'
END_DATE = '2025-07-31'
LAT = 33.44838
LON = -112.07404
OUTPUT = 'data/weatherDataPhoenix.csv'

if __name__ == '__main__':
    run_pipeline(LAT, LON, START_DATE, END_DATE, OUTPUT)