from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.http import HttpResponse

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False 
        user.save()
        
        current_site = get_current_site(self.request)
        mail_subject = 'Ative sua conta no Fórum Rede Silêncio'
        
        # Render HTML version
        html_content = render_to_string('registration/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        
        # Create Text version from HTML (or use separate template if preferred)
        # Here we use the separate .txt template as requested
        text_content = render_to_string('registration/account_activation_email.txt', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })

        to_email = form.cleaned_data.get('email')
        email = EmailMultiAlternatives(
            mail_subject, text_content, to=[to_email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        return redirect('account_activation_sent')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login') 
    else:
        return HttpResponse('Link de ativação inválido!')

class AccountActivationSentView(TemplateView):
    template_name = 'registration/account_activation_sent.html'
