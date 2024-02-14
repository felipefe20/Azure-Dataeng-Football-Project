# Football Data Engineering

## Table of Contents



## System Architecture

## Requirements
- Python 3.9 (minimum)
- Docker
- PostgreSQL
- Apache Airflow 2.6 (minimum)

## Getting Started

2. Install Python dependencies.
   ```bash
   pip install -r requirements.txt
   ```
   
## Running the Code With Docker

1. Start your services on Docker with
   ```bash
   docker compose up -d
   ``` 
2. Trigger the DAG on the Airflow UI.

## How It Works
1. Fetches data from Wikipedia.
2. Cleans the data.
3. Transforms the data.
4. Pushes the data to Azure Data Lake.

