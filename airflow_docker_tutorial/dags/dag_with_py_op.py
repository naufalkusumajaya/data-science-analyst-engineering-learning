import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def greet(name, admin):
    print(f' Hello {name}, My name is {admin}')

default_args = {
    'owner':'naufal',
    'retries':5,
    'retry_delay':datetime.timedelta(minutes=2)
} 
with DAG(
    dag_id='dag_with_py_op',
    description='wish me luck',
    default_args=default_args,
    start_date=datetime.datetime(2023,2,9),
    schedule_interval='57 1 * * *', # minute hour day(month) month day(week)
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs={'name':'Waltuh','admin':'Gustavo'}
    )
    task2 = PythonOperator(
        task_id="greet2",
        python_callable=greet,
        op_kwargs={'name':'There','admin':'Gustavo'}
    )
    task3 = PythonOperator(
        task_id="greet3",
        python_callable=greet,
        op_kwargs={'name':'Mike','admin':'Gustavo'}
    )
    
    [task2,task3] >> task1