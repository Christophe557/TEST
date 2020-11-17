from django import forms
from django.forms import ModelForm, TextInput
from .models import Quote


# Alternative avec Form:
#class QuoteForm(forms.Form):
#    texte = forms.CharField(widget=forms.Textarea)
#    auteur = forms.CharField()
#
#
# Avec ModelForm:
class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ["texte", "auteur"]
        widget = {
                'texte': TextInput(attrs={'class': 'form-control'}),
                'auteur': TextInput(attrs={'class': 'form-control'}),
                }

