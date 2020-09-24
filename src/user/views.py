from user.models import User
from user.forms import UserForm, ContactUsForm
from user.tasks import smth_slow_async
from user.utils import generate_random_password, smth_slow
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse


def generate_password(request):
    # request.args
    length = int(request.GET.get('len'))
    result = generate_random_password(length)
    return HttpResponse(str(result))


def users(request):
    # print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    context = {
        'user_list': User.objects.all(),
    }
    return render(request, 'list_users.html', context)


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('users-name'))
            return redirect('users-name')
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
            # return HttpResponseRedirect(reverse('users-name'))
            return redirect('users-name')
    elif request.method == 'GET':
        # instance == type(user) == User
        form = UserForm(instance=user)

    context = {
        'user_form': form,
        'user_instance': user,
    }
    return render(
        request,
        'create_user.html',
        context=context,
    )


def index(request):
    return render(request, 'index.html')


def slow(request):
    print('START')
    smth_slow_async.delay()
    print('END')
    return render(request, 'index.html')


def contact(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-name')
    elif request.method == 'GET':
        form = ContactUsForm()

    context = {
        'form': form,
    }
    return render(
        request,
        'contact_us.html',
        context=context,
    )