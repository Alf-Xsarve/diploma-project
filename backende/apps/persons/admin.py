from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import HistoricalPerson, Favorite, Profile


# 👤 Inline профиль (дата рождения)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


# 👤 Расширенный UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2"),
        }),
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Персональная информация", {
            "fields": ("first_name", "last_name", "email")
        }),
        ("Права доступа", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Важные даты", {
            "fields": ("last_login", "date_joined")
        }),
    )


# ❗ Перерегистрируем User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# 🧠 Исторические личности
@admin.register(HistoricalPerson)
class HistoricalPersonAdmin(admin.ModelAdmin):
    list_display = ("full_name", "birth_year", "death_year", "profession")
    search_fields = ("full_name", "profession")

    list_filter = ("profession", "birth_year")

    # 🔥 КРАСИВОЕ РАЗДЕЛЕНИЕ ФОРМЫ
    fieldsets = (
        ("Основная информация", {
            "fields": (
                "full_name",
                "profession",
                "birth_year",
                "death_year",
            )
        }),

        ("Описание", {
            "fields": (
                "description",
                "description_full",  # 🔥 НОВОЕ ПОЛЕ
            )
        }),

        ("Файлы и медиа", {
            "fields": (
                "photo",
                "doc_file",
                "pdf_file",
            )
        }),
    )


# ❤️ Избранное
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "person", "created_at")
    search_fields = ("user__username", "person__full_name")
    list_filter = ("created_at",)