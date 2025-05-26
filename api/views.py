from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate

# Временное хранилище для логина и пароля
TEMP_CREDENTIALS = {"username": None, "password": None}

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"success": False, "detail": "Username and password required"}, status=400)

    user = authenticate(username=username, password=password)
    if user is not None:
        TEMP_CREDENTIALS["username"] = username
        TEMP_CREDENTIALS["password"] = password
        return Response({"success": True})
    else:
        return Response({"success": False, "detail": "Invalid credentials"}, status=401)

@api_view(['GET'])
def get_credentials(request):
    if TEMP_CREDENTIALS["username"] and TEMP_CREDENTIALS["password"]:
        creds = TEMP_CREDENTIALS.copy()
        TEMP_CREDENTIALS["username"] = None
        TEMP_CREDENTIALS["password"] = None
        return Response(creds)
    else:
        return Response({"detail": "No credentials available"}, status=404)
