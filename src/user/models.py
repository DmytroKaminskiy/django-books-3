from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128, default='NONE')
    age = models.PositiveSmallIntegerField(default=0)

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def save(self, *args, **kwargs):
        print('User Model Before Save')
        # self.email = self.email.lower()
        # self.first_name = self.first_name.title()
        # self.last_name = self.last_name.title()
        super().save(*args, **kwargs)
        print('User Model After Save')


class GclidClick(models.Model):
    value = models.CharField(max_length=256, unique=True)
