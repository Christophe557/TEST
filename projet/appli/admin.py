from django.contrib import admin
from django.utils.text import Truncator

from .models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('apercu_texte', 'auteur', 'created_at')
    list_filter = ('auteur', 'created_at')
    search_fields = ('auteur', )

    def apercu_texte(self, quote):
        return Truncator(quote.texte).chars(40, truncate='...')

    apercu_texte.short_description = 'Aperçu de la citation'

admin.site.register(Quote, QuoteAdmin)

