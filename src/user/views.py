from django.shortcuts import render
from django.http import HttpResponse
from user.utils import generate_random_password
from faker import Faker

from user.models import User

# Create your views here.
def generate_password(request):
    # request.args
    length = int(request.GET.get('len'))
    result = generate_random_password(length)
    return HttpResponse(str(result))

# pip install django-extensions / ipython

def users(request):
    users = User.objects.all()
    results = ''
    for user in users:
        results += f'ID: {user.id}, Email: {user.email}'
    return HttpResponse(results)

def create_user(request):
    fake = Faker()
    user = User.objects.create(
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )
    return HttpResponse(f'ID: {user.id}, Email: {user.email}')
