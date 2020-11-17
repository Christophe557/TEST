from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Quote
from .forms import QuoteForm


def index(request):
    quotes = Quote.objects.order_by('-created_at')[:1]
    context = {'quotes': quotes}
    return render(request, 'appli/index.html', context)

def citations(request):
    quotes_list = Quote.objects.order_by('-created_at')
    # pagination avec url de type : appli/citations/?page=1
    paginator = Paginator(quotes_list, 5) # création de l'instance avec nombre de quotes par page 
    page = request.GET.get('page') # récupération du n°de la page courante de l'url /?page=3
    try:
        quotes = paginator.page(page) # groupe de quotes 
    except PageNotAnInteger:
        # si page n'est pas entier , on délivre la 1ère page:
        quotes = paginator.page(1)
    except EmptyPage:
        # si page out of range, on délivre la dernière page:
        quotes = paginator.page(paginator.num_pages)

    context = {
            'quotes': quotes,
            'paginate': True
            } 
    return render(request, 'appli/citations.html', context)

def citez(request):
    quotes = Quote.objects.order_by('-created_at')[:3]
    context = {'quotes': quotes}
    form = QuoteForm(request.POST or None)
    if form.is_valid():
        texte = form.cleaned_data["texte"]
        auteur = form.cleaned_data["auteur"]
        # attention : la méthode cleaned_data ne fonctionne qu'après
        # avoir appliqué la méthode is_valid

        new_quote = Quote.objects.create(
                texte=texte,
               auteur=auteur,
                )
        new_quote.save()
        context['new_quote'] = new_quote

        return render(request, 'appli/merci.html', context)

    context['form'] = form
    return render(request, 'appli/citez.html', context)

def apropos(request):
    # a supprimer??? - pas la peine de faire une vue pour ça ???
    return render(request, 'appli/apropos.html')


