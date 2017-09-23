from django.db import models
from django.utils import timezone

#Post è il nome del nostro modello, utilizzato per il blog
#models.Model significa che è un modello Django, quindi dovrebbe essere salvato
#nel DB
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
