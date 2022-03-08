from operator import itemgetter


cards = ['King', 3, 9, 4, 7, 1, 'Queen', 'King', 'Queen', 13, 'Jack']

"""
After my bad performance, I did a research on card deck (The common card game here does not have the QKJA cards)

I figured I should do the solution here, knowing it does not change my outcome.
"""


def sort_card_array(arr):
    card_str_map = [
        {'card': 'Jack', 'value':50},
        {'card': 'Queen', 'value':51},
        {'card': 'King', 'value':52}
        ]
    card_str_sort = sorted(card_str_map, key=itemgetter('value'))
    card_str_values = [s['card'] for s in card_str_sort]
    return sorted([x for x in cards if isinstance(x, int)]) + card_str_values

print(sort_card_array(cards))