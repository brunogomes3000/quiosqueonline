from django.contrib import admin
from .models import Usuario
from .models import Arte
from .models import Imagens

admin.site.register(Usuario)
admin.site.register(Arte)
admin.site.register(Imagens)
# Register your models here.
