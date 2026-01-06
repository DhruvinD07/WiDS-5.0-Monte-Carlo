from enum import Enum
import random

class Suits(Enum):
    SPADES = u'\u2660'
    HEARTS = u'\u2665'
    DIAMONDS = u'\u2666'
    CLUBS = u'\u2663'

class Card:
    def __init__(self, rank: str, suit: Suits):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if len(self.rank) == 2:  
            line2 = f"|{self.rank} |"
            line4 = f"| {self.rank}|"
        else:
            line2 = f"|{self.rank}  |"
            line4 = f"|  {self.rank}|"

        line1 = "_____"
        line3 = f"| {self.suit.value} |"
        line5 = "‾‾‾‾‾"

        return "\n".join([line1, line2, line3, line4, line5])
    
class Deck:
    def __init__(self):
        self.cards = []
        self.reset()
    
    def reset(self):
        self.cards = []
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in Suits:
            for rank in ranks:
                self.cards.append(Card(rank,suit))
        
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self) -> Card:
        if not self.cards:
            raise RuntimeError("Cannot draw from an empty deck")
        return self.cards.pop()
    
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def flush(self):
        self.cards = []

    def value(self) -> int:
        total = 0
        aces = 0

        for card in self.cards:
            if card.rank in ["J", "Q", "K"]:
                total += 10
            elif card.rank == "A":
                total += 11
                aces += 1
            else:
                total += int(card.rank)

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    
    def __str__(self):
        if not self.cards:
            return "<empty hand>"

        lines = ["", "", "", "", ""]

        for card in self.cards:
            card_rows = str(card).split("\n")
            for i in range(5):
                lines[i] += card_rows[i] + "  " 

        return "\n".join(lines)


