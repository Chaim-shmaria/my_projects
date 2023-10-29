from deck_of_cards import DeckOfCards


class Player(DeckOfCards):
    def __init__(self, name):
        super().__init__()
        self.name = str(name)
        self.hand = []
        self.score = 0

    def __repr__(self):
        return f"player: {self.name}"


class Game(Player, DeckOfCards):
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.deck = DeckOfCards()
        self.deck.shuffle()
        half_array = len(self.deck) // 2
        self.player1.hand.extend(self.deck[:half_array])
        self.player2.hand.extend(self.deck[half_array:])
        self.compare = None
        self.war_chest = None
        self.rounds = 0

    def war(self):
        self.war_chest = self.compare
        poping = [self.player1] * 3 + [self.player2] * 3
        for poper in poping:
            if len(poper.hand) > 1:
                self.war_chest.append(poper.hand.pop())
        return

    def round_play(self):
        while self.rounds < 100:
            if self.winner():
                print(self.winner().name)
                return self.winner()
            self.compare = []
            self.compare.append((self.player1.hand.pop(), self.player1))
            self.compare.append((self.player2.hand.pop(), self.player2))
            if self.compare[0] == self.compare[1]:
                self.war()
            if self.war_chest:
                max(self.compare)[1].score += 1
                max(self.compare)[1].hand.extend([item[0] for item in self.war_chest])
                max(self.compare)[1].hand.extend([item[0] for item in self.compare])
                self.war_chest = None
            else:
                max(self.compare)[1].score += 1
                max(self.compare)[1].hand.extend([item[0] for item in self.compare])
            self.compare = []
            self.rounds += 1
        return self.winner()

    def winner(self):
        if self.rounds >= 100:
            if self.player1.score == self.player2.score:
                return f"Both players are equal"
            else:
                winner = max((self.player1.score, self.player1), (self.player2.score, self.player2))
                return f"'{winner[1].name}' is the winner!"
        if len(self.player1.hand) < 1:
            return f"'{self.player2.name}' is the winner!"
        if len(self.player2.hand) < 1:
            return f"'{self.player1.name}' is the winner!"
        return None


war_game = Game('haim', 'avi')
print(war_game.round_play())
