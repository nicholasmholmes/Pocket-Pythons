class Poker:
    def __init__(self, players):
        self.players = players
        self.current_bet = 0
        self.pot = 0
        self.current_player_index = 0
        self.blinds = (1, 2)

    def get_current_player(self):
        return self.players[self.current_player_index]

    def advance_turn(self):
        # Move to the next player's turn
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def move_blinds(self):
        # Move the blinds to the next players
        self.players[0].stack -= self.blinds[0]
        self.players[1].stack -= self.blinds[1]
        self.pot += self.blinds[0] + self.blinds[1]

    def check(self, player: Player):
        # Checking is allowed if the current bet is 0 (no one has bet)
        if self.current_bet == 0:
            player.check()
            self.advance_turn()
        else:
            print(f"{player.name} cannot check. There is an active bet.")

    def fold(self, player: Player):
        player.fold()
        self.advance_turn()
        # Additional logic may be needed to handle removing the player from the active round

    def call(self, player: Player, amount):
        # Player calls the current bet
        if player.stack >= amount:
            player.call(amount)
            player.stack -= amount
            self.pot += amount
            self.advance_turn()
        else:
            print(f"{player.name} does not have enough chips to call.")

    def bet(self, player: Player, amount):
        # Betting involves setting a new current bet
        # Betting amounts will start at the big blind amount
        # After inital blinds players may bet in amounts of 1 big blind or higher, incrementing in halves
        # Players  
        if amount > self.current_bet:
            player.bet(amount)
            self.current_bet = amount
            player.stack -= amount
            self.pot += amount
            self.advance_turn()
        else:
            print(f"{player.name}'s bet must be higher than the current bet.")
