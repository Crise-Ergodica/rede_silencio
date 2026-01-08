from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/sent/', views.AccountActivationSentView.as_view(), name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
