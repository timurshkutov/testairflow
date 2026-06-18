from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2026, 6, 18),
}

with DAG(
    dag_id='test_dag_lol',
    default_args=default_args,
    schedule='@monthly',
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "YO HELLO"'
    )
