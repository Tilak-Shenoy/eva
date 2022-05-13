from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status 

from api.models import Voices
from api.serializers import ApiSerializers

# Create your views here.
# https://www.bezkoder.com/django-mongodb-crud-rest-framework/
# https://github.com/bezkoder/django-rest-api-mongodb
# GET list of voices, POST a new voices, DELETE all voices
@api_view(['GET', 'POST', 'DELETE'])
def get_save_or_delete_voice_list(request):
    if request.method == 'GET':
        voices = Voices.objects.all()
        voice_serializer = ApiSerializers(voices, many=True)
        return JsonResponse(voice_serializer.data, safe=False)
    elif request.method == 'POST':
        voice_data = JSONParser().parse(request)
        try:
            for voice in voice_data:
                voice_serializer = ApiSerializers(data=voice)
                if voice_serializer.is_valid():
                    voice_serializer.save()
            return JsonResponse(voice_data, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse(voice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Voices.objects.all().delete()
        return JsonResponse({'message': '{} Voices were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    



