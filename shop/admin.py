from django.contrib import admin

# Register your models here.
from .models import product
admin.site.register(product)

from .models import service

from .models import Categorie
admin.site.register(Categorie)


admin.site.register(service)

