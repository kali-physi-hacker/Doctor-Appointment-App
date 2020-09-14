from django.contrib import admin
from django.urls import path, include

from appointment.views.authentication import login, logout, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('authentication/login/', login, name="login"),
    path('authentication/logout/', logout, name="logout"),
    path('authentication/register/', register, name="register"),
]
