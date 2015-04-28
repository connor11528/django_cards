from django.db import models

# Create your models here.
class Card(models.Model):
    SPADE = 0
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SUITS = (
        (SPADE, "spade"),
        (CLUB, "club"),
        (DIAMOND, "diamond"),
        (HEART, "heart")
    )
    suit = models.PositiveSmallIntegerField(choices=SUITS)
    rank = models.CharField(max_length=5)