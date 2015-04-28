from django import template

register = template.Library()

# return first card
@register.filter
def first(list):
    if list is not None and len(list):
        return list[0]

# return only cards in the list with the given suit
@register.filter
def suit(list, suit_type):
    return [item for item in list if item.get_suit_display() == suit_type]