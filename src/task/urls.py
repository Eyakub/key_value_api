from django.urls import path

from .views import *


urlpatterns = [
    path('key-value', KeyValueView.as_view(), name='key_value'),
]