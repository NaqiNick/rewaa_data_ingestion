from django.utils import timezone
from rest_framework import serializers
from django.core.cache import cache

from sensor_data_ingestion.tasks import insert_data_async


class SensorPayloadSerializer(serializers.Serializer):
    collection_name = "sensor_data"

    sensor_id = serializers.IntegerField(required=True)
    value = serializers.SerializerMethodField()
    timestamp = serializers.DateTimeField(default=timezone.now())

    def get_value(self, value):
        return self.initial_data.get('value')

    def validate_dublicate_value(self, sensor_id, value):
        previous_value = cache.get(sensor_id)
        if value == previous_value:
            raise serializers.ValidationError({"value": "The current value from the sensor is the same as previous "
                                                        "value."})

    def cache_current_value(self, sensor_id, value):
        cache.set(sensor_id, value, timeout=60 * 5)

    def save(self, **kwargs):
        sensor_id = self.validated_data.get('sensor_id')
        value = self.initial_data.get('value')
        self.validate_dublicate_value(sensor_id=sensor_id, value=value)
        insert_data_async.delay(self.collection_name, self.data)
        self.cache_current_value(sensor_id=sensor_id, value=value)
