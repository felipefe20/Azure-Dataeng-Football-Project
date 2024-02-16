# Football Data Engineering-ETL

This project is about building a data pipeline for football data from fbref using Docker, PostgreSQL, Apache Airflow, and Azure Storage. It fetches, processes, and stores football data in a scalable and automated manner.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Docker
- Azure CLI
- Python 3.7 or higher

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/felipefe20/Azure-Dataeng-Football-Project.git
   
## Running the Code With Docker

1. Start your services on Docker with
   ```bash
   docker compose up -d
   ``` 


2. Register database in PostgreSQL
   ```bash
   http://localhost:5050
   ``` 

3. Create azure resources (ADLS) using Azure CLI


4. Trigger the DAG on the Airflow UI.
   ```bash
   http://localhost:8080
   ``` 

5. Load data to PostgreSQL and ADLS


## Pipeline
1. Fetches data from Fbref.
2. Cleans the data.
3. Transforms the data.
4. Loads data to PostgreSQL.
4. Pushes the data to Azure Data Lake.

