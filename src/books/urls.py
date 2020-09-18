from user import views as uv

from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    # path('', uv.index),
    path("", TemplateView.as_view(template_name='index.html'), name='index'),
    path('gp/', uv.generate_password),
    path('users/list/', uv.users, name='users-name'),
    path('cu/', uv.create_user, name='users-create'),
    path('users/<int:pk>/update/', uv.update_user, name='users-update'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
