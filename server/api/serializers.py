from rest_framework import serializers
from server.api.models import Voices

class ApiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Voices
        fields = (
            'id',
            'language',
            'country',
            'locale',
            'gender',
            'voice_name'
        )