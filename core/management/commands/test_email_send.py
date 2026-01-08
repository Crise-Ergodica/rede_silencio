from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Tests email sending configuration'

    def handle(self, *args, **options):
        self.stdout.write(f"Current backend: {settings.EMAIL_BACKEND}")
        try:
            send_mail(
                'Teste de Email Rede Silêncio (Command)',
                'Funciona! O backend está configurado corretamente.',
                'system@redesilencio.com',
                ['teste@example.com'],
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS('Email enviado com sucesso (veja o output acima)'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Falha no envio: {e}'))
