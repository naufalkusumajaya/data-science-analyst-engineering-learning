import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
import pytz

default_args = {
    'owner':'naufal',
    'retries':5,
    'retry_delay':datetime.timedelta(minutes=2)
}

with DAG(
    dag_id='dag_catchup_backfillv3',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='@daily',
    start_date=datetime.datetime(2023,2,1),
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo simple bash command'
    )