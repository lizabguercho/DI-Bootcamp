import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = self._build_deck()

    def _build_deck(self):
        deck = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for s in suits:
            for v in values:
                pairs = Card(s,v)
                deck.append(pairs)
        return deck
    
    def shuffle_cards(self):
        random.shuffle(self.cards)
        
    
    def deal_card(self):
       if not self.cards:
            raise ValueError ("No cards left in the")
       return self.cards.pop(random.randrange(len(self.cards)))
    
    def deal_hand(self,num_cards):
        hand = []
        for _ in range(num_cards):
            if self.cards:
                hand.append(self.deal_card())
        return hand



deck = Deck()
deck.shuffle_cards()
print(deck.deal_card())
print(len(deck.cards))
print(deck.deal_hand(5))
print(len(deck.cards))
