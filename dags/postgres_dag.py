from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import psycopg2

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

def create_table():
    conn = psycopg2.connect("dbname='postgres' user='airflow' host='tests_local-postgres-1' password='airflow'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test_table (id serial PRIMARY KEY, num integer, data varchar);")
    conn.commit()
    cur.close()
    conn.close()

dag = DAG('test_dag', default_args=default_args, description='A simple tutorial DAG',
          schedule_interval=None)

t1 = PythonOperator(
    task_id='create_table',
    python_callable=create_table,
    dag=dag,
)

t1