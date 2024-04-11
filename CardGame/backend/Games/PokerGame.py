from ..Components.Components import Player, Card, Deck, Rank

    
class PokerGame:

    def __init__(self, players: list[Player]) -> None:
        self.players      = players
        self.deck         = Deck()
        self.discard_pile = []
        self.has_ended    = False
        self.pot          = 0

    # Game Interactions
    def deal_card_to_player(self, player_to_get_card: Player, number_of_cards=1) -> None:
        for i in range(0, number_of_cards):
            top_card = self.deck.take_top_card()
            player_to_get_card.hand.append(top_card)

    def deal_new_hand(self, number_of_cards=5) -> None:
        for i in range(0, number_of_cards):
            for player_being_dealt_to in self.players:
                self.deal_card_to_player(player_being_dealt_to)

    def take_card_from_player(self, player_to_take_from: Player, card_position: int) -> None:
        taken_card = player_to_take_from.hand.pop(card_position)
        self.discard_pile.append(taken_card)
        
    def take_bet_from_player(self, player_to_take_from: Player, amount_to_take: int) -> None:
        player_to_take_from.bet(amount_to_take)
        self.pot += amount_to_take
        pass
    
    # Game Scoring
    def analyze_hand(self, hand: list[Card]) -> str:
        if self._is_royal_flush(hand): return "Royal Flush"
        if self._is_flush(hand) and self._is_straight(hand): return 'Straight Flush'
        if self._is_four_of_a_kind(hand): return 'Four of a Kind'
        if self._is_full_house(hand): return 'Full House'
        if self._is_flush(hand): return 'Flush'
        if self._is_straight(hand): return 'Straight'
        if self._is_three_of_a_kind(hand): return 'Three of a Kind'
        if self._is_two_pair(hand): return 'Two Pair'
        if self._is_pair(hand): return 'Pair'
        return  'High Card'
    
    def get_hand_score(self, hand: list[Card]) -> int:

        hands_ranking = [
            'Royal Flush',
            'Straight Flush',
            'Four of a Kind',
            'Full House',
            'Flush',
            'Straight',
            'Three of a Kind',
            'Two Pair',
            'Pair',
            'High Card'
        ]
        hands_ranking.reverse() # Built the list backwards, too lazy to fix right now
        hand_type = self.analyze_hand(hand)
        return 0 if hand_type not in hands_ranking else hands_ranking.index(hand_type)+1

    # All hand-value checks assume the hand is valid
    def _is_royal_flush(self, hand: list[Card]) -> bool:

        if not self._is_flush(hand): return False

        values = [Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING, Rank.ACE]
        for card in hand:
            if card.rank not in values: return False

        return True
    
    def _is_flush(self, hand: list[Card]) -> bool:
        suit = hand[0].suit
        for card in hand[1:]: 
            if card.suit != suit: return False
        return True
    
    def _is_straight(self, hand: list[Card]) -> bool:
        ranks = [card.rank.value for card in hand]
        ranks.sort()
        for rank in ranks:
            if rank != ranks[0]: return False
        return True

    def _n_of_a_kind(self, hand: list[Card]) -> list:
        of_a_kind = {}
        
        for card in hand:
            if card.rank not in of_a_kind:
                of_a_kind[card.rank] = 1
            else:
                of_a_kind[card.rank] += 1

        number_of_a_kind = [0 for i in range(0, 5)]
        for rank in of_a_kind:
            number_of_a_kind[of_a_kind[rank]] += 1

        return number_of_a_kind
    
    def _is_four_of_a_kind(self, hand: list[Card]) -> bool:
        return self._n_of_a_kind(hand)[4] > 0
    
    def _is_full_house(self, hand: list[Card]) -> bool:
        sets = self._n_of_a_kind(hand)
        return sets[2] == 1 and sets[3] == 1
    
    def _is_three_of_a_kind(self, hand: list[Card]) -> bool:
        return self._n_of_a_kind(hand)[3] > 0
    
    def _is_two_pair(self, hand: list[Card]) -> bool:
        return self._n_of_a_kind(hand)[2] == 2

    def _is_pair(self, hand: list[Card]) -> bool:
        return self._n_of_a_kind(hand)[2] == 1


