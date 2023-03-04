import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import sklearn

def sklearn_ver():
    print(sklearn.__version__)

default_args = {
    'owner':'naufal',
    'retries':5,
    'retry_delay':datetime.timedelta(minutes=2)
} 
with DAG(
    dag_id='sklearn_test',
    description='wish me luck',
    default_args=default_args,
    start_date=datetime.datetime(2023,2,11),
    schedule_interval='23 5 * * *', # minute hour day(month) month day(week)
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id="test",
        python_callable=sklearn_ver,
    )
    task1