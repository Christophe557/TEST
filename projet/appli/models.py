from django.db import models
from django.utils.text import Truncator

class Quote(models.Model):
    texte = models.TextField()
    auteur = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='date de parution')

    class Meta:
        verbose_name = "citation"

    def __str__(self):
        return Truncator(self.texte).chars(20, truncate='...')
