import pandas as pd

def transform_openmeteo_data(data):
    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "temp_max": data["daily"]["temperature_2m_max"],
        "temp_min": data["daily"]["temperature_2m_min"],
        "humidity_max": data["daily"]["relative_humidity_2m_max"],
        "humidity_min": data["daily"]["relative_humidity_2m_min"],
        "precipitation": data["daily"]["precipitation_sum"]
    })
    df["avg_temp"] = (df["temp_max"] + df["temp_min"]) / 2
    df["avg_humidity"] = (df["humidity_max"] + df["humidity_min"]) / 2
    return df[["date", "avg_temp", "avg_humidity", "precipitation", "temp_max", "temp_min"]]