
from django.contrib import admin
from django.urls import path, include

# para pegar as img que o usuario coloca no banco

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('empresa.urls')),
]
