class Card:
    def __init__(self, rank, suit):
        self.rank = rank # 1 = ace, 11 = jack, 12 = queen, 13 = king
        self.suit = suit

    def __str__(self):
        if self.rank == 1:
            return f"Ace of {self.suit}"
        elif self.rank == 11:
            return f"Jack of {self.suit}"
        elif self.rank == 12:
            return f"Queen of {self.suit}"
        elif self.rank == 13:
            return f"King of {self.suit}"
        return f"{self.rank} of {self.suit}"