from django.urls import path

from .views import *


urlpatterns = [
    path('values', KeyValueView.as_view(), name='values'),
]