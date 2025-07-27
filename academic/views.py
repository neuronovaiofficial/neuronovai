from django.shortcuts import render
from .models import Card

def cards(request):
    all_cards = Card.objects.all()
    return render(request, 'academic/cards.html', {'cards': all_cards})
