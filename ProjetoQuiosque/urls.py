
from django.conf.urls import url
from django.contrib import admin
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.index, name="index"),
    url(r'^resultadobuscar/$', views.resultadobuscar, name="resultadobuscar"),
    url(r'^arte_detalhes/$',views.arte_detalhes,name="arte_detalhes"),
    url(r'^gerenciararte/$',views.gerenciararte,name="gerenciararte"),
    url(r'^carrinho/$',views.carrinho,name="carrinho"),
    url(r'^edit_dados_pessoais/$',views.edit_dados_pessoais,name="edit_dados_pessoais"),
    url(r'^check_dados_pessoais/$',views.check_dados_pessoais,name="check_dados_pessoais"),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)