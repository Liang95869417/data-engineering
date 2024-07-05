from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Initialize the DAG
dag = DAG(
    'scheduling_data_pipeline',
    default_args=default_args,
    description='A example DAG for scheduling data pipeline',
    schedule=timedelta(days=1),
)

# Define the tasks
start_task = EmptyOperator(task_id='start_task', dag=dag)

def print_hello():
    return 'Hello world!'

hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

end_task = EmptyOperator(task_id='end_task', dag=dag)

# Set task dependencies
start_task >> hello_task >> end_task