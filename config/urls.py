from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from machina import urls as machina_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Rotas de login/logout/senha (Django padrão)
    path('accounts/', include('core.urls')), # Rotas customizadas (Registro, ativação, etc)
    path('forum/', include(machina_urls)), # ROTEAMENTO DAS URLS DO MACHINA (conecta o fórum inteiro)
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
]
