# Generated by Django 2.2.16 on 2020-09-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(default='NONE', max_length=128),
        ),
    ]