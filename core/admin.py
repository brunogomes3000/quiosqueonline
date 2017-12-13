from django.contrib import admin
from .models import Usuario
from .models import Arte
from .models import Imagens
from .models import Categoria

class ArteAdmin(admin.ModelAdmin):
	list_display = ['descricao', 'dataCadastro', 'email']
	list_filter = ['dataCadastro']
admin.site.register(Usuario)
admin.site.register(Arte, ArteAdmin)
admin.site.register(Imagens)
admin.site.register(Categoria)
# Register your models here.
