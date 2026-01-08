from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from machina import urls as machina_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include(machina_urls)), # ROTEAMENTO DAS URLS DO MACHINA (conecta o fórum inteiro)
    path('', RedirectView.as_view(url='/forum/', permanent=True)),
]
