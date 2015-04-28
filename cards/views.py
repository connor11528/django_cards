from django.shortcuts import render
from models import Card

# Create your views here.
def home(request):
	data = {
		'cards': Card.objects.all()
	}
	return render(request, 'cards.html', data)