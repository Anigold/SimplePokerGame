from enum import Enum
import random
from pprint import pprint
from typing import List
import os

os.system('') # Can also use os.system('Color')

Suit  = Enum('Suit', ['DIAMOND', 'HEART', 'CLUB', 'SPADE'])
Color = Enum('Enum', ['RED', 'BLACK'])
Rank  = Enum('Rank', [
    'TWO', 
    'THREE', 
    'FOUR', 
    'FIVE', 
    'SIX', 
    'SEVEN', 
    'EIGHT', 
    'NINE', 
    'TEN', 
    'JACK', 
    'QUEEN', 
    'KING',
    'ACE'])

class Shuffle(Enum):

    def _fisher_yates_shuffle(list_to_be_shuffled: list, seed=42) -> list:

        n = len(list_to_be_shuffled)
        for list_index in range(n-1, 0, -1):

            random_intance = random.Random(seed)
            random_pos     = random_intance.randint(0, list_index+1)

            list_to_be_shuffled[list_index], list_to_be_shuffled[random_pos] = list_to_be_shuffled[random_pos], list_to_be_shuffled[list_index]
        
        return list_to_be_shuffled
    
    def _random_shuffle(list_to_be_shuffled: list, seed=42) -> None:
        random.Random(seed).shuffle(list_to_be_shuffled)
        return list_to_be_shuffled
        
    FISHER_YATES   = _fisher_yates_shuffle
    RANDOM_SHUFFLE = _random_shuffle


class Card:

    def __init__(self, suit: Suit, rank: Color) -> None:
        self.suit  = suit
        self.rank  = rank

    def __repr__(self) -> str:
        return f'< Card {self.rank} of {self.suit} >'
    

class Deck:

    def __init__(self) -> None:
        self.cards = self._create_deck()

    def __repr__(self) -> str:
        return f'< Deck of Cards >'
    
    def shuffle(self, shuffle_type=Shuffle.RANDOM_SHUFFLE, iterations=5, seed=42) -> None:
        for i in range(0, iterations, 1):
            self.cards = shuffle_type(self.cards, seed)

    def _create_deck(self) -> list[Card]:
        cards = []
        for suit in Suit:
           for rank in Rank:
                cards.append(Card(suit, rank))
        return cards
    
    def take_top_card(self) -> Card:
        if not len(self.cards) > 0:
            raise IndexError('No top card.')
        
        return self.cards.pop(0)

# class Hand:
#     def __init__(self):
#         self.cards = []

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []
        self.cash = 0

    def __repr__(self) -> str:
        return f'< Player {self.name} >'  

    '''Bet an amount of cash or the total cash, whichever is greater.'''
    def place_bet(self, amount: int) -> int:
        return amount if amount <= self.cash else self.cash

class ComputerPlayer(Player):
    pass