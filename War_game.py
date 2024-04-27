import random
import os

suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace': 14}

def intro():
	print("Welcome to this game of War!")
	print("You will start with equal random set of cards.\nYou will then draw one card each to compare its value.")
	print("The player with higher value gets both set of cards.")
	print("Ultimately, the player with all the cards will win")
	print("Best of luck!")

def clear_screen():
	os.system('cls')

#setting up the cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

#setting up the deck
class Deck:
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#setting up the player
class Player:
    def __init__(self):
        self.name = input("\nPlease enter your name.")
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if new_cards == []:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards) 
    
    def __str__(self):
        return f'Player {self.name!r} has {len(self.all_cards)} cards.'


#setting up the game
if __name__ == '__main__':
	
	play_again = True

	while play_again:
	    play_again_input = ''
	    deck = Deck()
	    deck.shuffle()

	    player_1 = Player()
	    player_2 = Player()

	    clear_screen()

	    for i in range(26):
	        player_1.all_cards.append(deck.deal_one())
	        player_2.all_cards.append(deck.deal_one())

	    round = 0
	    game_on = True

	    print(f"\nThank you for joining us in this game {player_1.name!r} and {player_2.name!r}.")
	    print("\nLet us begin the game!")


	    while game_on:
	        round += 1
	        print(f'Round {round}')

	        if len(player_1.all_cards) == 0:
	            print("Player 1 is all out of cards, Player 2 wins!")
	            game_on = False
	            break

	        if len(player_2.all_cards) == 0:
	            print("Player 2 is all out of cards, Player 1 wins!")
	            game_on = False
	            break

	        player_1_cards = []
	        player_1_cards.append(player_1.remove_one())

	        player_2_cards = []
	        player_2_cards.append(player_2.remove_one())

	        at_war = True

	        
	        while at_war:

	            if player_1_cards[-1].value > player_2_cards[-1].value:
	                player_1.add_cards(player_1_cards)
	                player_1.add_cards(player_2_cards)
	                at_war = False

	            elif player_2_cards[-1].value < player_2_cards[-1].value:
	                player_2.add_cards(player_2_cards)
	                player_2.add_cards(player_1_cards)
	                at_war = False

	            else:
	                print("WAR!")

	                if len(player_1.all_cards) < 5:
	                    print("\nPlayer 1 does not have sufficient cards to war!")
	                    print(f"Player 2 {player_2.name!r} wins!")
	                    game_on = False
	                    break

	                elif len(player_2.all_cards) < 5:
	                    print("\nPlayer 2 does not have sufficient cards to war!")
	                    print(f"Player 1 {player_1.name!r} wins!")
	                    game_on = False
	                    break
	        
	                else:
	                    for num in range(5):
	                        player_1_cards.append(player_1.remove_one())
	                        player_2_cards.append(player_2.remove_one())


	    while play_again_input.lower() not in ['y', 'n']:

	        play_again_input = input("\nDo you want to play again? Enter 'Y' or 'N'.")
	        
	        try:
	            if play_again_input.lower() not in ['y', 'n']:
	                raise Exception("\nInappropriate input.")

	        except Exception:
	            print("\nPlease try again.")
	            continue


	        else:
	            if play_again_input.lower() == 'y':
	                print("\nGreat choice!")
	                play_again = True
	                continue
	            else:
	                print("\nThank you for playing!")
	                play_again = False
	                break