
from django.urls import path

from .views import index, greek

urlpatterns = [
  path('', index),
  path('greek/', greek)
]
