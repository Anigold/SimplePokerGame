from CardGame.frontend.ANSITerminal import ANSITerminal
from CardGame.backend.Components.Components import Player
from CardGame.backend.Games.PokerGame import PokerGame
import random


if __name__ == '__main__':
    
    terminal = ANSITerminal()
    #name = input('What is your name? \n')
    user_player = Player('Gabe')
    poker_game = PokerGame([user_player])
    intro = f'''

Welcome to the game, {terminal.color_text(user_player.name, "GREEN")}.

The game is a single hand of 5 card poker.

You will be dealt 5 cards; you may discard and receive \n up to 5 cards from the deck.

The player with the best hand wins.

Press ENTER to continue...

'''
    print(intro)
    print('')
    print(intro)
    user_input = 'NOT BLANK'
    while user_input != '':
        user_input = input('').strip()
    print('')

    
    poker_game.deck.shuffle(seed=random.randint(0, 92384))
    poker_game.deal_new_hand()


    print('\n'*10)
    print('Your hand:\n')
    for player in poker_game.players:
        for pos, card in enumerate(player.hand):
            print(pos+1, card)
    print('\n')
    print('Please list all cards you wish to discard (e.g. "1 3 5" to discard your 1st, 3rd, and 5th cards).')
    print('\n')
    while not poker_game.has_ended:

        discard_cards = input('')
        print('')
        new_hand = [i for i in user_player.hand]
        positions_to_discard = []
        for number in discard_cards.split(' '):
            if not number.isnumeric() or int(number)-1 < 0 or int(number)-1 > len(user_player.hand):
                print('Invalid input. Try again.')
                new_hand = [i for i in user_player.hand]
                break
            positions_to_discard.append(int(number)-1)
        
        positions_to_discard.sort(reverse=True) # Largest first so pop() doesn't affect the lower positions.

        for pos in positions_to_discard:
            poker_game.take_card_from_player(user_player, pos)

        poker_game.deal_card_to_player(user_player, number_of_cards=len(discard_cards.split(' ')))
        print('\n')
        print('Your hand:\n')
        for player in poker_game.players:
            for pos, card in enumerate(player.hand):
                print(pos+1, card)
        print('\n')

        print(poker_game.get_hand_score(user_player.hand))

        poker_game.has_ended = True







