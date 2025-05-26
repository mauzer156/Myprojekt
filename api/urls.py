from django.urls import path
from .views import login, get_credentials

urlpatterns = [
    path('login/', login, name='login'),
    path('credentials/', get_credentials, name='get_credentials'),
]
