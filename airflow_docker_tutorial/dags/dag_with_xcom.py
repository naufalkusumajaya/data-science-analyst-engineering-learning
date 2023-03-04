import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def greet(ti):
    name = ti.xcom_pull(task_ids='name_admin', key='name')
    admin = ti.xcom_pull(task_ids='name_admin', key='admin')
    circadian = ti.xcom_pull(task_ids='time', key='circadian')
    print(f'Good {circadian} \n Hello {name}\n My name is {admin}')

def get_name_admin(ti):
    ti.xcom_push(key='name', value='Paidi')
    ti.xcom_push(key='admin', value='Gustavo')

def get_time(ti):
    ti.xcom_push(key='circadian', value='Morning')

default_args = {
    'owner':'naufal',
    'retries':5,
    'retry_delay':datetime.timedelta(minutes=2)
} 
with DAG(
    dag_id='dag_with_xcom',
    description='wish me luck',
    default_args=default_args,
    start_date=datetime.datetime(2023,2,9),
    schedule_interval='36 2 * * *', # minute hour day(month) month day(week)
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
    )
    task2 = PythonOperator(
        task_id="name_admin",
        python_callable=get_name_admin,
    )
    task3 = PythonOperator(
        task_id="time",
        python_callable=get_time,
    )
    
    [task2,task3] >> task1