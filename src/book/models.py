from django.db import models
from user.models import User


class Book(models.Model):
    title = models.CharField(max_length=128)
    # author = models.ForeignKey('user.User', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        related_name='books',
        on_delete=models.CASCADE,
    )
