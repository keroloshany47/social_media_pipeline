from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import etl_pipeline

with DAG(
    dag_id="social_media_etl",
    description="ETL pipeline for social media (Twitter + YouTube)",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["etl", "social_media"]
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=etl_pipeline,
        op_kwargs={"query": "sport"}
    )

    run_etl
