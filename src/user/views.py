from user.models import User
from user.forms import UserForm
from user.utils import generate_random_password
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect, Http404

from faker import Faker


def generate_password(request):
    # request.args
    length = int(request.GET.get('len'))
    result = generate_random_password(length)
    return HttpResponse(str(result))


def users(request):
    users = User.objects.all()
    results = ''
    for user in users:
        results += f'ID: {user.id}, Email: {user.email}'
    return HttpResponse(results)


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/')
    elif request.method == 'GET':
        form = UserForm()

    context = {'user_form': form}
    return render(
        request,
        'create_user.html',
        context=context,
    )


def update_user(request, pk):

    # try:
    #     user = User.objects.get(pk=pk)
    # except User.DoesNotExist:
    #     raise Http404

    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/')
    elif request.method == 'GET':
        # instance == type(user) == User
        form = UserForm(instance=user)

    context = {'user_form': form}
    return render(
        request,
        'create_user.html',
        context=context,
    )
