from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CabinetClickLogSerializer

@api_view(['POST'])
def track_cabinet_click(request):
    serializer = CabinetClickLogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Временное хранилище для логина и пароля
TEMP_CREDENTIALS = {"username": None, "password": None}

@api_view(['GET'])
def latest_user(request):
    """
    Возвращает последнего зарегистрированного пользователя (по ID).
    """
    try:
        user = User.objects.latest('id')
        return Response({
            "username": user.username,
            "email": user.email
        })
    except User.DoesNotExist:
        return Response({"detail": "No users found"}, status=404)

@csrf_exempt
@api_view(['POST'])
def login(request):
    """
    Получает логин и пароль от расширения, проверяет в базе данных.
    """
    username = request.data.get("username")
    password = request.data.get("password")

    print(f"\n🔌 Получены данные от расширения:")
    print(f"    ➤ username: {username}")
    print(f"    ➤ password: {password}")

    if not username or not password:
        print("⛔ Не передан логин или пароль")
        return Response(False, status=400)

    try:
        user = User.objects.get(username=username)
        print(f"📦 Данные из БД для {username}:")
        print(f"    ➤ username: {user.username}")
        print(f"    ➤ hashed password (из базы): {user.password}")

        # Проверка пароля вручную
        if check_password(password, user.password):
            print("✅ Пароль совпадает (check_password)")

            # Сохраняем во временное хранилище
            TEMP_CREDENTIALS["username"] = username
            TEMP_CREDENTIALS["password"] = password

            return Response(True)
        else:
            print("❌ Пароль НЕ совпадает (check_password)")
            return Response(False, status=401)

    except User.DoesNotExist:
        print("❌ Пользователь не найден в базе")
        return Response(False, status=401)

@api_view(['GET'])
def get_credentials(request):
    """
    Возвращает последние сохранённые логин и пароль и обнуляет хранилище.
    """
    if TEMP_CREDENTIALS["username"] and TEMP_CREDENTIALS["password"]:
        creds = TEMP_CREDENTIALS.copy()
        TEMP_CREDENTIALS["username"] = None
        TEMP_CREDENTIALS["password"] = None
        return Response(creds)
    else:
        return Response({"detail": "No credentials available"}, status=404)
