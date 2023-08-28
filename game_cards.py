from random import randrange


def create_deck():
    suits = ['s', 'h', 'd', 'c']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = list()
    for suit in suits:
        for value in values:
            deck.append(f'{value}{suit}')
    return deck


def shuffle_deck(deck):
    new_deck = deck.copy()
    for i in range(0, len(deck)):
        other_index = randrange(0, len(new_deck))
        new_deck[i], new_deck[other_index] = new_deck[other_index], new_deck[i]
    return new_deck


def deal(players, cards, deck):
    if players * cards > len(deck):
        return deck

    table = list()

    for _ in range(0, cards):
        for player in range(0, players):
            if player >= len(table):
                table.append([deck.pop()])
            else:
                table[player].append(deck.pop())
    return table


init_desk = create_deck()
desk = shuffle_deck(init_desk)
table = deal(4, 6, desk)
print(table)
