import os
from pathlib import Path

# Constrói o caminho base do projeto (raiz onde está o manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# AVISO DE SEGURANÇA: Mantenha esta chave secreta em produção!
SECRET_KEY = 'django-insecure-mjhztj$1r5_raw@&d--8_uq&3x4l+4wp**h35hjdeqh54wu5=7'

# Mude para False se for colocar o site no ar (produção)
DEBUG = True

ALLOWED_HOSTS = []

# --- APLICATIVOS INSTALADOS ---
INSTALLED_APPS = [
    # Apps Padrão do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Dependências do Machina
    'mptt',
    'haystack',
    'widget_tweaks',

    # O Pacote Machina
    'machina',

    # Apps do Machina (ESTA LISTA É OBRIGATÓRIA E NA ORDEM CERTA)
    'machina.apps.forum',
    'machina.apps.forum_conversation',
    'machina.apps.forum_conversation.forum_attachments',
    'machina.apps.forum_conversation.forum_polls',
    'machina.apps.forum_feeds',
    'machina.apps.forum_moderation',
    'machina.apps.forum_search',
    'machina.apps.forum_tracking',
    'machina.apps.forum_member',
    'machina.apps.forum_permission',
    'core',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Middleware do Machina (Permissões de acesso)
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
    
    # Custom Force Login
    'core.middleware.AuthRequiredMiddleware',
]

ROOT_URLCONF = 'config.urls'

# --- TEMPLATES (HTML) ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # IMPORTANTE: Aponta para a pasta 'templates' na raiz do projeto
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # Processador de contexto do Machina (Metadados do fórum)
                'machina.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# --- BANCO DE DADOS ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- CACHE ---
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    # O Machina EXIGE essa configuração específica aqui:
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'machina_attachments',
    },
}

# --- VALIDAÇÃO DE SENHA ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# --- INTERNACIONALIZAÇÃO ---
LANGUAGE_CODE = 'pt-br'  # Mudado para Português do Brasil
TIME_ZONE = 'America/Sao_Paulo' # Fuso horário de Brasília
USE_I18N = True
USE_TZ = True

# --- ARQUIVOS ESTÁTICOS E MÍDIA ---
STATIC_URL = 'static/'
# STATICFILES_DIRS = [BASE_DIR / 'static'] # Descomente se criar a pasta static na raiz
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# Configuração para Uploads (Imagens, Anexos do fórum)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CONFIGURAÇÕES DO MACHINA ---

# Motor de busca (SimpleEngine é apenas para desenvolvimento local)
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

MACHINA_FORUM_NAME = "Rede Silêncio"
MACHINA_FORUM_DESCRIPTION = "Fórum de discussão da Rede Silêncio"
MACHINA_DEFAULT_PAGE_SIZE = 20

# --- CONFIGURAÇÕES DO CORE / AUTH ---
LOGIN_REDIRECT_URL = '/forum/'
LOGOUT_REDIRECT_URL = '/forum/'

# Para desenvolvimento, imprime o email no terminal
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Permissões padrão para novos usuários (ex: podem postar)
MACHINA_DEFAULT_AUTHENTICATED_USER_PERMISSIONS = [
    'can_see_forum',
    'can_read_forum',
    'can_start_new_topics',
    'can_reply_to_topics',
    'can_edit_own_posts',
    'can_post_without_approval',
    'can_create_polls',
    'can_vote_in_polls',
    'can_download_file',
]