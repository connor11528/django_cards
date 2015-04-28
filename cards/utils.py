from models import Card

def create_deck():
    """
    Create a list of playing cards in our database
    """
    suits = [0, 1, 2, 3]
    ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
    cards = [Card(suit=suit, rank=rank) for rank in ranks for suit in suits]
    Card.objects.bulk_create(cards)