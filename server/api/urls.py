from api import views
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^api/api$', views.get_save_or_delete_voice_list)
]