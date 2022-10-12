import random
import time
import emoji
from random import shuffle

spade = (emoji.emojize(':spades:', language = 'alias'))
club = (emoji.emojize(':clubs:', language = 'alias'))
heart = (emoji.emojize(':hearts:', language = 'alias'))
diamond = (emoji.emojize(':diamonds', language = 'alias'))

suits = {spade: 1, club: 2, heart: 3, diamond: 4}
ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


player_turn = True ############################################################################


def newgame():

    global club
    global spade
    global heart
    global diamond

    # Deck
    global deck
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)

    shuffle(deck)

    #Player's hand
    global playerhand
    playerhand = []

    for num in range(1, 9):
        playerhand.append(deck[0])
        deck.pop(0)

    playerspade = []
    playerclub = []
    playerheart = []
    playerdiamond = []

    for card in playerhand:
        if card[-1] == spade:
            playerspade.append(card)

        elif card[-1] == club:
            playerclub.append(card)

        elif card[-1] == heart:
            playerheart.append(card)

        else:
            playerdiamond.append(card)


    playerhand = playerspade + playerheart + playerclub + playerdiamond

    # Bot's hand
    global bothand
    bothand = []

    for num in range(1, 9):
        bothand.append(deck[0])
        deck.pop(0)

    botspade = []
    botclub = []
    botheart = []
    botdiamond = []

    for card in bothand:
        if card[-1] == spade:
            botspade.append(card)

        elif card[-1] == club:
            botclub.append(card)

        elif card[-1] == heart:
            botheart.append(card)
        else:
            botdiamond.append(card)

    bothand = botspade + botheart + botclub + botdiamond

    # Trump
    global trumpsuit

    trumpcard = deck[0]
    trumpsuit = trumpcard[-2]
    deck.pop(0)

def display_test():
    print(f"\nCards left: {len(deck)}")
    print(f"Trump suit: {trumpsuit}")
    print(f"Bot's hand: {len(bothand)}")
    print(f"Player's hand: {(playerhand)}\n")
    print(f'Attacking cards: {attackingcards}')
    print(f'Defending cards: {defendingcards}')

playedcards = []
attackingcards = []
defendingcards = []



newgame()
