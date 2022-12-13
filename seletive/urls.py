from django.contrib import admin
from django.urls import path, include

# para pegar as img que o usuario coloca no banco
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('empresa.urls')),
    path('vagas/', include('vagas.urls')),
    path('', include('empresa.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
