import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'naufal',
    'retries':5,
    'retry_delay':datetime.timedelta(minutes=2)
} 
with DAG(
    dag_id='our_first_dagv2',
    description='wish me luck',
    default_args=default_args,
    start_date=datetime.datetime(2023,2,9),
    schedule_interval='56 1 * * *', # minute hour day(month) month day(week)
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello, i am the first task"
    )
    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo hello, i am the second task"
    )
    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo hello, i am the third task"
    )
    
    task1 >> [task2,task3]