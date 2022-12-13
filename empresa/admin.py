from django.contrib import admin

from .models import Empresa, Tecnologias, Vagas

# Register your models here.
admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)
