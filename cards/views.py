from django.shortcuts import render
from models import Card

# Create your views here.
def home(request):
	data = {
		'cards': Card.objects.all()
	}
	return render(request, 'cards.html', data)

def test_filter(request):
	data = {
		'cards': Card.objects.all()
	}
	return render(request, 'test_filter.html', data)

def blackjack(request):
    data = {
        'cards': Card.objects.order_by('?')[:2]
    }

    return render(request, 'blackjack.html', data)

def poker(request):
    data = {'cards': Card.objects.order_by('?')[:5]}

    return render(request, 'poker.html', data)