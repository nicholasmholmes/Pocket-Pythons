from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['diamonds', 'hearts', 'clubs', 'spades']:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))
        self.count = 52
    
    def shuffle(self):
        pass # call shuffle algorithm

    def deal_card(self):
        self.count -= 1
        return self.cards.pop()
    
