from django.contrib import admin

# Register your models here.
from .models import product
admin.site.register(product)

from .models import service

from .models import Categorie
admin.site.register(Categorie)

from .models import reservation
admin.site.register(reservation)


admin.site.register(service)

