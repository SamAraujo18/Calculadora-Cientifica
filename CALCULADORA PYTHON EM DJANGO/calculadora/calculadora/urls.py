from django.contrib import admin
from django.urls import path
from core.views import home, calcular

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('calcular/', calcular, name='calcular'),
]