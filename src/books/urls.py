from django.contrib import admin
from django.urls import path

from user import views as uv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gp/', uv.generate_password),
    path('users/', uv.users),
    path('cu/', uv.create_user),
]
