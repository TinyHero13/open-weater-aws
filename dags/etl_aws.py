from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load

with DAG(
    'etl_open_weather_aws',
    start_date = datetime(2025, 1, 11),
    schedule_interval = '@daily',
    default_args = {
        'owner': 'Yasmim',
        'retries': 3
    },
    catchup = False,
    tags = ['aws', 'etl', 'open_weather', 'api']
) as dag:
    
    extract_task = PythonOperator(
        task_id = 'extract',
        python_callable = extract
    )

    transform_task = PythonOperator(
        task_id = 'transform',
        python_callable = transform,
        op_kwargs = {'task_id': 'extract'}
    )

    load_task = PythonOperator(
        task_id = 'load',
        python_callable = load,
        op_kwargs = {'task_id': 'transform'}
    )

    extract_task >> transform_task >> load_task