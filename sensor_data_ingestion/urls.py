from django.urls import path

from sensor_data_ingestion.views import post_sensor_data

urlpatterns = [
    path('post/', post_sensor_data, name='sensor-data-post'),
]