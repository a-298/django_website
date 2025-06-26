import random
from django.shortcuts import render
from quotes.models import Quote


def quotes(request):
    entries = Quote.objects.all()
    random_quote = random.choice(entries)
    return render(request, "quotes.html", {"quote": random_quote})
