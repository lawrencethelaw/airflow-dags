from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("👋 Hello from Airflow!")

with DAG(
    dag_id="hello_world",
    start_date=datetime(2025, 6, 27),
    schedule_interval="@once",
    catchup=False,
    tags=["test"],
) as dag:
    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello
    )