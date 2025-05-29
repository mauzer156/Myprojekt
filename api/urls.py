
from django.urls import path
from .views import track_cabinet_click, login, get_credentials, latest_user

urlpatterns = [
    path('log/', track_cabinet_click, name='track-click'),
    path('login/', login, name='login'),
    path('get_credentials/', get_credentials, name='get-credentials'),
    path('latest_user/', latest_user, name='latest-user'),
]
