from typing import Any

class Player:
    def __init__(self, name, hole_cards):
        self.name = name
        self.hole_cards = hole_cards
        self.stack = 0
        self.player_action = None

    def check(self):
        self.player_action = "check"

    def fold(self):
        self.player_action = "fold"

    def call(self, amount):
        self.player_action = "call"

    def bet(self, amount):
        self.player_action = "bet"

    def reset_action(self):
        # Resets the player's action to None at the start of a new round
        self.player_action = None
