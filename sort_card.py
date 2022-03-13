from operator import itemgetter


cards = ['King', 3, 9, 4, 7, 1, 'Queen', 'King', 'Queen', 13, 'Jack']

"""
sort a list of integers and strings; ints(ascending) and strs(Jack, Queen, King)

Expected outcome of above list: [1, 3, 4, 7, 9, 13, 'Jack', 'King', 'Queen']
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
