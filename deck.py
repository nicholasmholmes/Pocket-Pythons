from card import Card
from random import random, randint

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['diamonds', 'hearts', 'clubs', 'spades']:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))
        self.discards = []

    def __str__(self):
        returnstr = ''
        for card in self.cards:
            returnstr += str(card) + '\n'
        return returnstr
    
    def _riffle_shuffle(self):
        shuffled_deck = []
        approx_half = len(self.cards) // 2 + randint(-4, 4)
        half1 = self.cards[:approx_half]
        half2 = self.cards[approx_half:]
        while half1 or half2:
            if not half1:
                shuffled_deck.extend(half2)
                half2 = []
                break
            elif not half2:
                shuffled_deck.extend(half1)
                half1 = []
                break
            if random() > .5 + (randint(-100, 100)/1000):
                shuffled_deck.append(half1.pop(0))
            else:
                shuffled_deck.append(half2.pop(0))
        self.cards = shuffled_deck

    def shuffle(self):
        self.cards.extend(self.discards) # self.discards will be empty originally, but will add back all cards dealt to hands, burnt, or to the river on top
        self.discards = []
        for _ in range(7):
            self._riffle_shuffle()
        cut = randint(10, 42)
        self.cards = self.cards[cut:] + self.cards[:cut]
        

    def deal_card(self):
        card = self.cards.pop()
        self.discards.append(card)
        return card
    



    
def test():
    deck = Deck()
    print('Deck before shuffle:')
    print(deck)
    print('Deck after shuffle:')
    deck.shuffle()
    print(deck)

test()