import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

print(f"Current Email Backend: {settings.EMAIL_BACKEND}")

try:
    print("Attempting to send test email...")
    send_mail(
        'Teste de Email Rede Silêncio',
        'Se você está lendo isso, o sistema de email (Console) está funcionando.\nLink: http://127.0.0.1:8000/teste',
        'system@redesilencio.com',
        ['user@example.com'],
        fail_silently=False,
    )
    print("Email sent successfully (check the output above!).")
except Exception as e:
    print(f"Error sending email: {e}")
