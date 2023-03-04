import datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner':'naufal',
    'retries':5,
    'retry_delay':datetime.timedelta(minutes=2)
}

with DAG(
    dag_id='dag_pg_opv3',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='23 15 * * *',
    start_date=datetime.datetime(2023,2,10),
    catchup=False
) as dag:
    task1 = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='pg_docker',
        sql="""
            CREATE TABLE IF NOT EXISTS dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt,dag_id)
            );
        """
    )
    task1