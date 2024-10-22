from poker import Poker
from player import Player
from deck import Deck
from card import Card


class GameHandler:
    def __init__(self, players):
        self.game = Poker(players)
        self.deck = Deck()
    
    def start_game(self):
        self.deck.shuffle()
        self.game.move_blinds()
    
