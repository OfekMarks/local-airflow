from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id='my_first_dag',
    start_date=datetime(1970, 1, 1),
    schedule_interval='@once'
) as my_first_dag:
    print_task = PythonOperator(
        task_id='print_task',
        python_callable=lambda: print('This is running from my local airflow environment!')
    )
