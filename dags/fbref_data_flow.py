import os
import sys
from datetime import datetime

import pandas as pd
import soccerdata as sd

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.fbref_getting_data_pipeline import process_team_season_stats


dag = DAG(
    dag_id='fbref_data_flow',
    default_args={
        "owner": "Felipe Fernandez",
        "start_date": datetime(2023, 12, 18),
    },
    schedule_interval=None,
    catchup=False
)


leagues="Big 5 European Leagues Combined"
seasons="2022"


fbref = sd.FBref(leagues=leagues, seasons=seasons)

extract_team_season_stats = PythonOperator(
    task_id='process_team_season_stats',
    python_callable=process_team_season_stats,
    provide_context=True,
    op_args=[fbref, 'standard'],  
    dag=dag
)

extract_team_season_stats
