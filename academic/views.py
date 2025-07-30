from django.shortcuts import render
from .models import Card

def cards(request):
    all_cards = Card.objects.all().order_by('-created_at')  # 🟢 Sıralama eklendi
    return render(request, 'academic/cards.html', {'cards': all_cards})

