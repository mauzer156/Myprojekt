from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Временное хранилище для логина и пароля
TEMP_CREDENTIALS = {"username": None, "password": None}

@api_view(['GET'])
def latest_user(request):
    try:
        user = User.objects.latest('id')
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
            return Response(True)
        else:
            print("❌ Пароль НЕ совпадает (check_password)")
            return Response(False, status=401)

    except User.DoesNotExist:
        print("❌ Пользователь не найден в базе")
        return Response(False, status=401)

@api_view(['GET'])
def get_credentials(request):
    if TEMP_CREDENTIALS["username"] and TEMP_CREDENTIALS["password"]:
        creds = TEMP_CREDENTIALS.copy()
        TEMP_CREDENTIALS["username"] = None
        TEMP_CREDENTIALS["password"] = None
        return Response(creds)
    else:
        return Response({"detail": "No credentials available"}, status=404)
