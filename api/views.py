from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User  # ✅ Вот это надо было добавить!

# Временное хранилище для логина и пароля
TEMP_CREDENTIALS = {"username": None, "password": None}

@api_view(['GET'])
def latest_user(request):
    try:
        user = User.objects.latest('id')  # ✅ Работает только если User импортирован
        return Response({
            "username": user.username,
            "email": user.email
        })
    except User.DoesNotExist:
        return Response({"detail": "No users found"}, status=404)

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(False, status=400)  # неверный запрос

    user = authenticate(username=username, password=password)
    if user is not None:
        return Response(True)
    else:
        return Response(False, status=401)  # неверные данные

@api_view(['GET'])
def get_credentials(request):
    if TEMP_CREDENTIALS["username"] and TEMP_CREDENTIALS["password"]:
        creds = TEMP_CREDENTIALS.copy()
        TEMP_CREDENTIALS["username"] = None
        TEMP_CREDENTIALS["password"] = None
        return Response(creds)
    else:
        return Response({"detail": "No credentials available"}, status=404)
