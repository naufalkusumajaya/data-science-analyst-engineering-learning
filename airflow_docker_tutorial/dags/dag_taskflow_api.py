import datetime

from airflow.decorators import dag, task

default_args = {
    'owner':'naufal',
    'retries':5,
    'retry_delay':datetime.timedelta(minutes=2)
}

@dag(
    dag_id='dag_taskflow_apiv1',
    default_args=default_args,
    start_date=datetime.datetime(2023,2,9),
    schedule_interval='52 15 * * *'
)
def hello_world_etl():
    
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name':'Jeffrey',
            'last_name':'Bezoz'
        }
    @task()
    def get_age():
        return (2023 - 1964)
    @task
    def greeting(first_name, last_name, age):
        print(f"Hello {first_name} {last_name}, Your age is {age}")
        
    name_dict = get_name()
    age = get_age()
    greeting(first_name=name_dict['first_name'], 
             last_name=name_dict['last_name'],
             age=age)
    
greet_dag = hello_world_etl()