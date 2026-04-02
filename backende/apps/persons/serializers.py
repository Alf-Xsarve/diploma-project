from django.contrib.auth.models import User
from rest_framework import serializers
from .models import HistoricalPerson, Favorite, Profile


# 👤 Пользователь
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


# 🔐 Регистрация
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password_confirm = serializers.CharField(write_only=True)

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    birth_date = serializers.DateField(required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'birth_date',
            'password',
            'password_confirm',
        ]

    # 🔍 Проверка паролей
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    # ❌ Проверка username
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Пользователь уже существует")
        return value

    # ❌ Проверка email
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email уже используется")
        return value

    # 💾 Создание пользователя
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password_confirm')

        birth_date = validated_data.pop('birth_date', None)

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        # 🔥 безопасная работа с профилем
        profile, created = Profile.objects.get_or_create(user=user)

        if birth_date:
            profile.birth_date = birth_date
            profile.save()

        return user


# 🧠 Историческая личность
class HistoricalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerson
        fields = [
            'id',
            'full_name',
            'birth_year',
            'death_year',
            'profession',
            'description',
            'description_full',  # 🔥 НОВОЕ ПОЛЕ
            'photo',
            'doc_file',
            'pdf_file'
        ]


# ❤️ Избранное
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user', 'person', 'created_at']
        read_only_fields = ['user', 'created_at']