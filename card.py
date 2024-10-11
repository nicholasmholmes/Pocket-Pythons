class Card:
    def __init__(self, rank, suit):
        self.rank = rank # 14 = ace, 11 = jack, 12 = queen, 13 = king
        self.suit = suit

    def __str__(self):
        if self.rank == 14:
            return f"Ace of {self.suit}"
        elif self.rank == 11:
            return f"Jack of {self.suit}"
        elif self.rank == 12:
            return f"Queen of {self.suit}"
        elif self.rank == 13:
            return f"King of {self.suit}"
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __gt__(self, other):
        return self.rank > other.rank
    
    def __le__(self, other):
        return self.rank <= other.rank
    
    def __ge__(self, other):
        return self.rank >= other.rank
    
    def __ne__(self, other):
        return self.rank != other.rank
    
