import random
import tqdm
from deck_of_cards import DeckOfCards, Card


def log(*args, **kwargs):
    """
    Conditionally print messages to the console if LOG is True.
    """
    if LOG:
        print(*args, **kwargs)


def argmax(arr, key):
    """
        Returns all elements in the input list 'arr' that have the
        maximum value, according to the provided key function.
    """
    # assert all(isinstance(e.top, Card) for e in arr)
    elem = max(arr, key=key)
    return [e for e in arr if key(e) == key(elem)]


def chunks(arr, n):
    """
    Yield successive n-sized chunks from arr.
    """
    k = len(arr) // n
    arr = arr[:k * n]
    for i in range(0, len(arr), k):
        yield arr[i:i + k]


def flat(arr: list):
    """ Flatten a list of lists, shuffle the elements, and return a new list."""
    arr = sum(arr, [])
    random.shuffle(arr)
    return arr


class Player:

    def __init__(self, id):
        """Initialize a player with a unique ID."""
        self.id = id
        self.hand = []
        self.taken = 0

    def __repr__(self):
        """Return a string representation of the player."""
        return str(self.id)

    def initialize_hand(self, cards):
        """Initialize the player's hand with a list of cards."""
        assert all(isinstance(c, Card) for c in cards)
        self.hand = cards

    def play_cards(self, war=False):
        """Play cards from the player's hand, up to 4 in a war situation."""
        # if random.random() < .2:
        #     random.shuffle(self.hand)
        if not war:
            self.top = self.hand.pop(0)
            return [self.top]
        n = min(len(self.hand), 4)
        cards = self.hand[:n]
        self.hand = self.hand[n:]
        if self.hand:
            self.top = self.hand[-1]
        return cards

    def add_cards(self, cards):
        """Add a list of cards to the player's hand and update the 'taken' count."""
        self.hand += cards
        self.taken += 1
        log(f'Player {self.id} took the round')

    def has_cards(self):
        """Check if the player has any cards left in their hand."""
        return bool(self.hand)


class WarGame:

    def __init__(self, num_players=2):
        """Initialize the WarGame with the specified number of players."""
        self.players = [Player(i) for i in range(num_players)]
        self.deck = DeckOfCards()
        self.deck.shuffle()
        self.deal_cards()
        self.game_over = False
        self.round = 0

    def update_players_status(self):
        """Update the status of players, check for losers, and end the game if there's a winner."""
        lost = []
        for player in self.players:
            log(f'player {player.id} has {len(player.hand)} cards in his hand')
            if not player.has_cards():
                log(f'>>>> Player {player} lost')
                lost.append(player)

        self.players = [p for p in self.players if p not in lost]
        if len(self.players) == 1:
            log(f'**** Player {self.players[0]} Won the game!!')
            self.game_over = True

    def deal_cards(self):
        """Evenly deal cards to the players from the shuffled deck."""
        p = len(self.players)
        n = len(self.deck)
        k = n // p
        for player in self.players:
            hand = self.deck.deal_hand(k)
            player.initialize_hand(hand)

    def play_round(self):
        """Play a round of the game."""
        self.update_players_status()
        if self.game_over:
            return
        self.round += 1
        log(f'round: {self.round}' + '-' * 50)
        winner = war = False
        players = self.players
        table = []
        while not winner:
            if self.has_deadlock(players):
                return self.resolve_deadlock(flat(table))
            table += [p.play_cards(war=war) for p in players]
            round_winner = argmax(players, key=lambda p: p.top)
            if len(round_winner) == 1:
                winner = round_winner[0]
            war = True
            players = round_winner
        winner.add_cards(flat(table))

    def resolve_deadlock(self, table):
        """Resolve a deadlock situation by randomly splitting the cards in the table."""
        random.shuffle(table)
        n = len(self.players)
        for player, cards in zip(self.players, chunks(table, n)):
            player.add_cards(cards)
        log('Deadlock resolved by randomly splitting the cards in the table')

    def has_deadlock(self, players):
        """Check if all players have run out of cards, leading to a deadlock."""
        for p in players:
            if p.has_cards():
                return False
        return True

    def play(self):
        """Play the game until it's over."""
        while not self.game_over:
            self.play_round()
        log(f'Game Over in Round {self.round}')

    def winner(self):
        """Return the winner of the game, assuming there is one."""
        return self.players[0]


LOG = False
# LOG = True

num_players = 2
winners = {i: 0 for i in range(num_players)}
rounds = []
n = int(1e4)
for _ in tqdm.trange(n):
    game = WarGame(num_players)
    game.play()
    winners[game.winner().id] += 1
    rounds.append(game.round)
print(winners)
print(sum(rounds) / n)
