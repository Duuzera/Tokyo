from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('incluir.urls')),
    path('', include('perfil.urls')),
    path('', include('historico.urls')),
]
