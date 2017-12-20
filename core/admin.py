from django.contrib import admin
from .models import Usuario
from .models import Arte
from .models import Categoria
from .models import cartaoCredito

class ArteAdmin(admin.ModelAdmin):
	list_display = ['descricao', 'dataCadastro', 'usuario']
	list_filter = ['dataCadastro']
admin.site.register(Usuario)
admin.site.register(Arte, ArteAdmin)
admin.site.register(Categoria)
admin.site.register(cartaoCredito)
# Register your models here.
