#### ERRRORRR

# import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# import psycopg2

# conn = psycopg2.connect(
#     database="airflow_pg_conn",
#     host='localhost',
#     user='airflow',
#     password='airflow',
#     port='5433'
# )

# def insert(sql):
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()

# default_args = {
#     'owner':'naufal',
#     'retries':5,
#     'retry_delay':datetime.timedelta(minutes=2)
# } 
# with DAG(
#     dag_id='connect_pg_local',
#     description='wish me luck',
#     default_args=default_args,
#     start_date=datetime.datetime(2023,2,11),
#     schedule_interval='24 4 * * *', # minute hour day(month) month day(week)
#     catchup=False
# ) as dag:
#     task1 = PythonOperator(
#         task_id="insert1",
#         python_callable=insert,
#         op_kwargs={'sql':"""
#                    INSERT INTO testing (val) VALUES
#                     ('1'),('rabbit')
#                    """}
#     )
#     task2 = PythonOperator(
#         task_id="insert2",
#         python_callable=insert,
#         op_kwargs={'sql':"""
#                    INSERT INTO testing (val) VALUES
#                     ('2'),('rabbit')
#                    """}
#     )
#     task3 = PythonOperator(
#         task_id="insert3",
#         python_callable=insert,
#         op_kwargs={'sql':"""
#                    INSERT INTO testing (val) VALUES
#                     ('3'),('rabbit')
#                    """}
#     )
    
#     [task2,task3] >> task1