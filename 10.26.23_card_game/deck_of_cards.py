# edited: 10.19.23
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"(Card: {self.rank} {self.suit})"

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank


class DeckOfCards:
    def __init__(self):
        self.deck = []
        self.creat_deck()
        self.popped_element = None

    def creat_deck(self):
        suits = ['diamond', 'club', 'heart', 'spade']
        for suit in suits:
            for rank in range(1, 14):
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        # self.popped_element = self.deck.pop(0)
        return self.deck.pop(0)

    def __len__(self):
        return len(self.deck)

    def __str__(self):
        human_readable_deck = []
        card_num = 0
        for card in self.deck:
            card_num += 1
            human_readable_deck.append(f"card number {card_num}: suit = {card.suit}, rank = {card.rank}")
        return human_readable_deck

    def __getitem__(self, item):
        return self.deck[item]

    def sort_by_suit(self):
        return self.deck.sort(key=lambda x: x.suit)

    def sort_by_rank(self):
        return self.deck.sort(key=lambda x: x.rank)

    def joker(self):
        pass

    def deal_hand(self, cards_num):
        cards_to_deal = []
        for i in range(cards_num):
            cards_to_deal.append(self.draw())
        return cards_to_deal

    def count_cards(self):
        counter = [0] * 13
        for card in self.deck:
            counter[card.rank - 1] += 1
        return counter


temp = DeckOfCards()
temp.shuffle()

# for card in temp.deck:
#     print(card)
temp_player = temp.deal_hand(5)

# print('\n' * 5)

# print(temp.deck[0].rank, temp.deck[1].rank, temp.deck[0].__lt__(temp.deck[1]))
