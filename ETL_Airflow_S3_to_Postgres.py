from airflow import DAG
from airflow.operator.python import PythonOperator
from datetime import datetime, timedelta
import boto3
import pandas as pd
import psycopg2

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    "etl_s3_to_postgres",
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

# Extract the data from S3
def extract_from_s3():
    s3=boto3.client('s3')
    s3.download_file('bucket_name', 'data.csv', '/tmp/data.csv')

extract = PythonOperator(
    task_id='extract',
    python_callable=extract_from_s3,
    dag=dag
)

# Transform the date column to the format of '%d-%m-%y'
def transform_data():
    df = pd.read_csv('/tmp/data.csv')
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    df.to_csv('/tmp/transformed_data.csv', index=False)

transform = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag
)

# Load the data to postgres sql
def load_to_postgres():
    conn = psycopg2.connect("db=db username=username password=password host=myhost")
    cur = conn.cursor()
    df = pd.read_csv('/tmp/transformed_data.csv')

    for _, row in df.iter_rows():
        cur.execute("INSERT INTO sale(id, amount, date) VALUES(%s, %s, %s)",
                    (row['id'], row['amount'], row['date']))

    conn.commit()
    cur.close()
    conn.close()

load = PythonOperator(
    task_id='load',
    python_callable=load_to_postgres,
    dag=dag
)

# Task Dependencies
extract >> transform >> load






