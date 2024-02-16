import os
import sys
from datetime import datetime

import pandas as pd
import soccerdata as sd

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.fbref_getting_data_pipeline import process_team_season_stats

from airflow.models import Variable

import logging

dag = DAG(
    dag_id='fbref_data_flow',
    default_args={
        "owner": "Felipe Fernandez",
        "start_date": datetime(2023, 12, 18),
    },
    schedule_interval=None,
    catchup=False
)


leagues = Variable.get("leagues", default_var="Big 5 European Leagues Combined")
seasons = Variable.get("seasons", default_var="2022")
stat_type = Variable.get("stat_type", default_var="standard")

# Set up logging
logging.basicConfig(level=logging.INFO)

# Log the current values of the variables
logging.info(f'Leagues: {leagues}')
logging.info(f'Seasons: {seasons}')
logging.info(f'Stat type: {stat_type}')


fbref = sd.FBref(leagues=leagues, seasons=seasons)

extract_team_season_stats = PythonOperator(
    task_id='process_team_season_stats',
    python_callable=process_team_season_stats,
    provide_context=True,
    op_args=[fbref, stat_type],  
    dag=dag
)

extract_team_season_stats
