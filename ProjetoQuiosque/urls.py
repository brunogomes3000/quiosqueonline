
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
    url(r'^editarArte/$',views.editarArte,name="editarArte"),
    url(r'^editarDadosPessoais/$',views.editarDadosPessoais,name="editarDadosPessoais"),
    url(r'^checkDadosPessoais/$',views.checkDadosPessoais,name="checkDadosPessoais"),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)