from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import json

def process_data_func():
    raw_data = '{"events": ["login", "click", "purchase", "login"]}'
    data = json.loads(raw_data)
    count = len(data['events'])
    print(f"Processed {count} events successfully!")

with DAG(
    dag_id='complex_etl_dag',
    default_args={'start_date': datetime(2026, 6, 18)},
    schedule='@daily',
    catchup=False
) as dag:

    start_task = BashOperator(
        task_id='start_task',
        bash_command='echo "Starting ETL pipeline..."'
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=process_data_func
    )

    end_task = BashOperator(
        task_id='end_task',
        bash_command='echo "ETL pipeline finished!"'
    )

    start_task >> transform_task >> end_task
