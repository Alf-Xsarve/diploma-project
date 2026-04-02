from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# 👤 Профиль пользователя (расширение User)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    birth_date = models.DateField("Дата рождения", null=True, blank=True)

    def __str__(self):
        return f"Профиль: {self.user.username}"


# 🧠 Историческая личность
class HistoricalPerson(models.Model):
    full_name = models.CharField("ФИО", max_length=200)
    birth_year = models.IntegerField("Год рождения")
    death_year = models.IntegerField("Год смерти", blank=True, null=True)
    profession = models.CharField("Профессия", max_length=100)

    # 📄 Описания
    description = models.TextField("Краткое описание")
    description_full = models.TextField("Полное описание", blank=True)  # 🔥 НОВОЕ ПОЛЕ

    photo = models.ImageField(
        "Фотография",
        upload_to="persons_photos/",
        blank=True,
        null=True
    )

    # 📄 Документы
    doc_file = models.FileField(
        "Документ Word",
        upload_to="persons_docs/",
        blank=True,
        null=True
    )
    pdf_file = models.FileField(
        "Документ PDF",
        upload_to="persons_pdfs/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.full_name


# ❤️ Избранное
class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    person = models.ForeignKey(
        HistoricalPerson,
        on_delete=models.CASCADE,
        related_name="favorited_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "person")

    def __str__(self):
        return f"{self.user.username} → {self.person.full_name}"


# 🔥 СИГНАЛ (вынесен наружу — так правильно!)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)