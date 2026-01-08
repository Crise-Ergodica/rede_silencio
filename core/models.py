from django.db import models
from django.conf import settings
from machina.apps.forum_conversation.models import Post

class GhostPost(models.Model):
    """
    Extension for Machina Post to allow 'Ghost' posting (fake identity).
    Linked via OneToOne to the original Post.
    """
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        related_name='ghost_post',
        verbose_name='Post original'
    )
    fake_username = models.CharField(
        max_length=150, 
        blank=True, 
        null=True, 
        help_text="Nome falso para exibir no lugar do usuário real"
    )
    fake_avatar = models.ImageField(
        upload_to='ghost_avatars/', 
        blank=True, 
        null=True,
        help_text="Avatar falso para exibir"
    )

    def __str__(self):
        return f"Ghost info for post {self.post_id}"
