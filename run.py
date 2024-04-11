from CardGame.frontend.ANSITerminal import ANSITerminal
from CardGame.backend.Components.Components import Player, ComputerPlayer
from CardGame.backend.Games.PokerGame import PokerGame
import random


if __name__ == '__main__':
    
    terminal = ANSITerminal()
    #name = input('What is your name? \n')

    # Create players
    players     = [ComputerPlayer(f'{i}') for i in range(0, 3)]
    user_player = Player('Gabe')
    players.append(user_player)

    # Give players starting cash
    for player in players:
        player.cash = 100

    # Create game object
    poker_game = PokerGame(players)

    intro = f'''

Welcome to the game, {terminal.color_text(user_player.name, "GREEN")}.

The game is a single hand of 5 card poker.

You will be dealt 5 cards; you may discard and receive \n up to 5 cards from the deck.

The player with the best hand wins.

Press ENTER to continue...

'''
    print('')
    print(intro)
    user_input = 'NOT BLANK'
    while user_input != '':
        user_input = input('').strip()
    print('')

    
    poker_game.deck.shuffle(seed=random.randint(0, 92384))
    poker_game.deal_new_hand()

    # Display hands of all non-computer players
    print('\n'*10)
    for player in poker_game.players:
        if not isinstance(player, ComputerPlayer):
            print(player)
            print('-'*15)
            for pos, card in enumerate(player.hand):
                print(pos+1, card)
            print('')
    print('\n')

    # Get players initial bets
    for player in poker_game.players:
        bet_size = 1 # Computers will always bet 1 for now.
        if not isinstance(player, ComputerPlayer):
            bet_size = int(input(f'{player.name}, place your intital bet: '))
        player.place_bet(bet_size)
        poker_game.pot += bet_size

    print(f'\nTotal pot size is: {poker_game.pot}')

    # Offer players to discard and get new cards
    print('\n')
    for player in poker_game.players: 
        discard_cards = '1 2' # Computers will always discard the first two cards for now.
        if not isinstance(player, ComputerPlayer):
            discard_cards = input(f'{player.name}, please list all cards you wish to discard (e.g. "1 3 5" to discard your 1st, 3rd, and 5th cards).')
        
        new_hand = [i for i in player.hand]
        positions_to_discard = []

        # If the player doesn't want to discard any cards, go to the next player.
        if not discard_cards.strip(): continue

        for number in discard_cards.split(' '):
            if not number.isnumeric() or int(number)-1 < 0 or int(number)-1 > len(player.hand):
                print('Invalid input. Game over, loser.')
                new_hand = [i for i in player.hand]
                break
            positions_to_discard.append(int(number)-1)
        
        positions_to_discard.sort(reverse=True) # Largest first so pop() doesn't affect the lower positions.

        for pos in positions_to_discard:
            poker_game.take_card_from_player(player, pos)

        poker_game.deal_card_to_player(player, number_of_cards=len(discard_cards.split(' ')))

    # Display hands of all players
    print('\n'*10)
    for player in poker_game.players:
        if not isinstance(player, ComputerPlayer):
            print(player)
            print('-'*15)
            for pos, card in enumerate(player.hand):
                print(pos+1, card)
            print('')
    print('\n')

    # Get 2nd round of betting
    for player in poker_game.players:
        bet_size = 1 # Computers will always bet 1 for now.
        if not isinstance(player, ComputerPlayer):
            bet_size = int(input(f'{player.name}, place your bet: '))
        player.place_bet(bet_size)
        poker_game.pot += bet_size

    print(f'\nTotal pot size is: {poker_game.pot}')

    # Score hands, announce winner
    winning_players = []
    winning_hand_score = 0
    for player in poker_game.players:
        hand_type = poker_game.analyze_hand(player.hand)
        hand_score = poker_game.get_hand_score(player.hand)

        if hand_score > winning_hand_score:
            winning_players = [player]
            winning_hand_score = hand_score
        elif hand_score == winning_hand_score:
            winning_players.append(player)

        print(player)
        print('-'*15)
        for pos, card in enumerate(player.hand):
            print(pos+1, card)
        print(hand_type)
        print('')

    print(f'Winners: {[player.name for player in winning_players]}')


    # while not poker_game.has_ended:

    #     discard_cards = input('')
    #     print('')
    #     new_hand = [i for i in user_player.hand]
    #     positions_to_discard = []
    #     for number in discard_cards.split(' '):
    #         if not number.isnumeric() or int(number)-1 < 0 or int(number)-1 > len(user_player.hand):
    #             print('Invalid input. Try again.')
    #             new_hand = [i for i in user_player.hand]
    #             break
    #         positions_to_discard.append(int(number)-1)
        
    #     positions_to_discard.sort(reverse=True) # Largest first so pop() doesn't affect the lower positions.

    #     for pos in positions_to_discard:
    #         poker_game.take_card_from_player(user_player, pos)

    #     poker_game.deal_card_to_player(user_player, number_of_cards=len(discard_cards.split(' ')))
    #     print('\n')
    #     print('Your hand:\n')
    #     for player in poker_game.players:
    #         for pos, card in enumerate(player.hand):
    #             print(pos+1, card)
    #     print('\n')

    #     print(poker_game.get_hand_score(user_player.hand))

    #     poker_game.has_ended = True







