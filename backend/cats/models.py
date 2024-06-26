"""Это документация для вашего модуля."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Achievement(models.Model):
    """Brief description of YourClass."""

    name = models.CharField(max_length=64)

    def __str__(self):
        """Brief description of YourClass."""
        return self.name


class Cat(models.Model):
    """Brief description of YourClass."""

    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE
    )
    achievements = models.ManyToManyField(Achievement,
                                          through='AchievementCat')
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None
    )
    """Brief description of YourClass."""

    def __str__(self):
        """Brief description of YourClass."""
        return self.name


class AchievementCat(models.Model):
    """Brief description of YourClass."""

    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        """Brief description of YourClass."""
        return f'{self.achievement} {self.cat}'
