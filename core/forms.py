from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GhostPost

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Digite um endereço de e-mail válido.')

    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class GhostPostForm(forms.ModelForm):
    class Meta:
        model = GhostPost
        fields = ['fake_username', 'fake_avatar']
