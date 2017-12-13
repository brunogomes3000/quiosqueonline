
from django.conf.urls import url
from django.contrib import admin
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
from django.contrib.auth.views import logout





urlpatterns =   [
	url(r'^$', views.index, name="index"),
    url(r'^resultadobuscar/$', views.resultadobuscar, name="resultadobuscar"),
    url(r'^arte_detalhes/$',views.arte_detalhes,name="arte_detalhes"),
    url(r'^gerenciararte/$',views.gerenciararte,name="gerenciararte"),
    url(r'^carrinho/$',views.carrinho,name="carrinho"),
    url(r'^editarArte/$',views.editarArte,name="editarArte"),
    url(r'^enviarArte/$',views.enviarArte,name="enviarArte"),
    url(r'^editarDadosPessoais/$',views.editarDadosPessoais,name="editarDadosPessoais"),
    url(r'^checkDadosPessoais/$',views.checkDadosPessoais,name="checkDadosPessoais"),
    url(r'^usuario/$', views.usuario, name="usuario"),
    url(r'^sobre/$', views.sobre, name="sobre"),
    url(r'^login/$', login, {'template_name':'login.html'}, name ="login"),
    url(r'^sair/$', logout, {'next_page': '/'}, name="logout"),
    url(r'^admin/', admin.site.urls),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)