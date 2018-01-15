from functools import total_ordering
import random

@total_ordering
class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5','6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])

    def mate(self):
        if self.suit == 0:
            card = Card(3, self.rank)
        if self.suit == 1:
            card = Card(2, self.rank)
        if self.suit == 2:
            card = Card(1, self.rank)
        if self.suit == 3:
            card = Card(0, self.rank)
        return card

    def __lt__(self, other):
        if self.rank < other.rank: return True
        if self.rank > other.rank: return False
        return self.suit < other.suit

    def __eq__(self, other):
        return ((self.rank == other.rank) and (self.suit == other.suit)) 

#This is the Deck Object. It allows you to create a Deck from the Cards.
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

#This is the Hand Object. It inherits from Deck. It allows you to create a Hand from the Deck.
class Hand(Deck):
 def __init__(self,label=''):
     self.cards = []
     self.label = label


mydeck = Deck()
mydeck.shuffle()
myhand = Hand('New Hand')
mycard = mydeck.pop_card()
myhand.add_card(mycard)
print (myhand.label)
print (myhand)
mydeck.move_cards(myhand,4)
print (myhand.label)
print (myhand)
