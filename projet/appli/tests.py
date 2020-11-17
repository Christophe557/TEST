from django.test import TestCase
from django.urls import reverse

from .models import Quote

#----------------------------------------------
# Page index
class IndexPageTestCase(TestCase):

    def test_index_page(self):
        #test que la page d'accueil renvoie bien le code 200
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
#----------------------------------------------
# Page citations
class CitationsPageTestCase(TestCase):

    def test_citations_page_return_200(self):
        #test que la page des citations renvoie bien le code 200
        response = self.client.get(reverse('appli:citations'))
        self.assertEqual(response.status_code, 200)
        

#----------------------------------------------
# Page citez
class CitezPageTestCase(TestCase):

    def setUp(self):
        #création d'un exemple de test
        quote_test = Quote.objects.create(texte='blabla', auteur='Bibi')
        self.quote = Quote.objects.get(texte='blabla')
    
    def test_citez_page_return_200(self):
        #test que la page citez renvoie bien le code 200
        response = self.client.get(reverse('appli:citez'))
        self.assertEqual(response.status_code, 200)

    def test_new_quote_is_registered(self):
        #test qu'une nouvelle citation est bien enregistrée dans la BD
        old_quotes = Quote.objects.count() # nombre citations dans BD
        quote_id = self.quote.id #nouvelle citation
        texte = self.quote.texte 
        auteur= self.quote.auteur
        response = self.client.post(
            reverse('appli:citez'),
            {'texte':texte, 'auteur':auteur}
            )
        new_quotes = Quote.objects.count() # nombre citations dans BD
        self.assertEqual(new_quotes, old_quotes+1)

#----------------------------------------------
# Page apropos
class AproposPageTestCase(TestCase):

    def test_apropos_page(self):
        #test que la page a propos renvoie bien le code 200)
        response = self.client.get(reverse('appli:apropos'))
        self.assertEqual(response.status_code, 200)
        

