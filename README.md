# WeatherWise-ETL

WeatherWise-ETL is an ETL (Extract, Transform, Load) pipeline designed to automate the processing of weather data. This project demonstrates how to fetch raw weather datasets, apply data transformations, and store the results for further analysis. The modular structure supports extensibility for different data sources and transformation logic.

Further enhancement includes - leverage the CSV as data source, and plot charts for visualizations using POWER BI.

## What We Learned

- **ETL Concepts:** Implemented the full ETL cycle—extracting data from Openmeteo APIs, transforming it for consistency and usability, and loading it into a CSV file.
- **Data Engineering:** Explored best practices for organizing code, handling data pipelines, and ensuring data quality.
- **Python Programming:** Used Python for scripting, modularization, and leveraging libraries for data manipulation.
- **API Integration:** Learned how to interact with external APIs to fetch real-time weather data.
- **Data Transformation:** Applied cleaning, normalization, and enrichment techniques to raw datasets.
- **Project Structure:** Practiced organizing a scalable codebase for collaborative development.
- **GitHub Collaboration:** How to collaborate with other engineer using GitHub
- **POWER BI:** Learned how to use POWER BI and plot charts for visualization

## Tech Stack

- **Language:** Python 3.x
- **Libraries:** pandas, requests (see `requirements.txt` for full list)
- **File Formats:** CSV for data storage and processing
- **Version Control:** Git
- **IDE:** Visual Studio Code

## Project Structure

```
.gitignore
LICENSE
README.md
requirements.txt
run_etl.py
.vscode/
data/
    weatherData.csv
    weatherDataPhoenix.csv
etl/
    pipeline.py
utils/
    api.py
    transform.py
```

- **data/**: Contains sample weather datasets.
- **etl/pipeline.py**: Main ETL pipeline implementation.
- **utils/api.py**: Utilities for API interactions.
- **utils/transform.py**: Data transformation utilities.
- **run_etl.py**: Script to execute the ETL pipeline.
- **requirements.txt**: Python dependencies.
- **LICENSE**: MIT License.

## Getting Started

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Run the ETL pipeline:**
    ```sh
    python run_etl.py
    ```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author

Copyright (c) 2025 Sachin Bhardwaj, Stuti Pandey
