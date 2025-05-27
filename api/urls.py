from django.urls import path
from .views import login, get_credentials, latest_user

urlpatterns = [
    path('login/', login),
    path('get-credentials/', get_credentials),
    path('latest-user/', latest_user),  # 👈 добавили
]

