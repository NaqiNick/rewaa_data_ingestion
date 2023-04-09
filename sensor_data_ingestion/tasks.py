from celery import shared_task

from sensor_data_ingestion.mongodb_api import insert_document


@shared_task
def insert_data_async(collection_name, document):
    insert_document(collection_name, document)