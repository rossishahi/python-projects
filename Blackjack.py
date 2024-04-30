# importing necessary modules
import random
import os


# global variables
playing = True
suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
    'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


# function to clear output screen
def clear_screen():
    return os.system('cls')


# class to handle individual card details
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


# class to handle a deck of cards
class Deck:

    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# class to manage player and dealer hands
class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        if self.value > 21 and self.aces > 1:
            self.value -= 10
            self.aces -= 1
            print("Value adjusted for Ace!")


# class to manage the chips
class Chips():

    def __init__(self):

        self.total = ''

        while not str(self.total).isdigit():
            try:
                self.total = int(
                    input("\nEnter the starting amount of chips."))
            except:
                print("\nInvalid amount entered. Please try again.")
                continue
            else:
                clear_screen()
                print(f"Starting amount of chips: {self.total}")
                
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        print("\nCongratulations, you have WON the bet!")
        print(f'Chips WON: {self.bet}.')

    def lose_bet(self):
        self.total -= self.bet
        print('\nUnfortunately, you have LOST the bet!')
        print(f'Chips LOST: {self.bet}')

    def reset_chips(self):
    	pass


# functions to show cards
def show_some(player, dealer):
    print("\nShowing some cards:")
    print("\nPlayer cards")
    print("*"*13)

    for pos, card in enumerate(player.cards):
        print(f'\tCard {pos+1}: {card}')

    print("\nDealer cards")
    print("*"*13)
    print('\tCard 1: Hidden')
    print(f'\tCard 2: {dealer.cards[1]}')


def show_all(player, dealer):
    print("\nShowing all cards:")
    print("\nPlayer cards")
    print("*"*13)

    for pos, card in enumerate(player.cards):
        print(f'\tCard {pos+1}: {card}')
    print(f"\n\tTotal value of cards: {player.value}")

    print("\nDealer cards")
    print("*"*13)
    for pos, card in enumerate(dealer.cards):
        print(f'\tCard {pos+1}: {card}')
    print(f"\n\tTotal value of cards: {dealer.value}")


# function to take bets
def take_bet(chips):

    player_bet = ''

    while not str(player_bet).isdigit() or player_bet > chips.total:
        try:
            player_bet = int(input("\nPlease enter your betting amount."))

        except:
            print("Please enter valid amount.")
            continue

        else:
            if player_bet > chips.total:
                print("Betting amount cannot be more than available amount.")
                continue
            else:
                chips.bet = player_bet
                
    
    clear_screen()
    
    print(f'\nPlayer has bet: {player_bet}')


#function to add card when hitting
def hit(deck, hand):
    hand.add_card(deck.deal_one()) 


#function to decide between hit or stand
def hit_or_stand(deck, hand):

    global playing
    
    hit_stand = ''

    while playing:

        while hit_stand.lower() not in ['h', 's']:
            try:
                hit_stand = input("\nDo you wish to 'Hit' or 'Stand'. Please enter 'H' or 'S'.")
                
                if hit_stand.lower() not in ['h', 's']:
                    raise Exception("Invalid input!")

            except Exception:
                print("Please try again!")
                continue
            
            except:
                print("Please try again!")
                continue
            

            else:
                clear_screen()
                
                if hit_stand.lower()  == 'h':
                    print("\nPlayer has decided to 'Hit'.")
                    hit(deck, hand)
                    print("A new card has been added to the Player's hand!")
                    playing = False
                    break
                
                else:
                    print("\n\tPlayer has decided to 'Stand'.")
                    playing = False


#functions to decide outcome based on win/lose/bust
def player_busts(chips):
    print("\nPlayer BUSTED! Dealer WINS!")
    chips.lose_bet()
    
def player_wins(chips):
    print("\nPlayer WINS! Dealer LOST!")
    chips.win_bet()    

def dealer_busts(chips):
    print("\nDealer BUSTED! Player WINS!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("\nDealer WINS! Player LOST!")
    chips.lose_bet()

def no_win():
    print("\nIt is a draw between Player and Dealer!")


#main py execution
if __name__ == '__main__':
    game_on = True
    
    while game_on:
        
        playing = True
        
        #setting up the deck
        deck = Deck()
        deck.shuffle()
        
        #setting up the player and dealer hands
        player = Hand()
        dealer = Hand()
        
        #setting up the chips and starting bet
        chips = Chips()
        take_bet(chips)
        
        #dealing two cards each to player and dealer
        for item in range(2):
            player.add_card(deck.deal_one())
            dealer.add_card(deck.deal_one())
            
	    #showing cards dealt
        show_some(player, dealer)
        
	    
        #Case 1: Natural win in two cards - Player wins
        if player.value == 21 and dealer.value != 21:
            show_all(player, dealer)
            player_wins(chips)
            playing = False
            
	    
        #Case 2: Both have natural blackjack - Tie
        elif player.value == dealer.value == 21:
            no_win()
            playing = False
            
	    #checking win or lose
        while playing:
	        
	        #asking to hit or stand
            hit_or_stand(deck, player)
            show_some(player, dealer)
            
	        #adjusting for aces if any
            player.adjust_for_aces()
            
	        
            #Case3 : Player bust
            if player.value > 21:
                show_all(player, dealer)
                player_busts(chips)
                break
            
            if dealer.value < 17:
                
	        #checking for dealer; deal until dealer's sum is more than 17
                print("\nDealer's hand is lower than 17. Dealer will hit!")
            
            while dealer.value <= 17:
                hit(deck, dealer)
                print("\tA new card added to Dealer's hand!")
                
            show_all(player, dealer)
            
	        
            #Case 4: Dealer bust
            if dealer.value > 21:
                dealer_busts(chips)
                break
            
	        
            #Case 5: Dealer wins
            elif player.value < dealer.value < 21:
                dealer_wins(chips)
                break
            
            
            #Case 6: Player wins
            elif dealer.value < player.value < 21:
                player_wins(chips)
                break
            
            
            #Case 7: Another tie
            elif dealer.value == player.value:
                no_win()
                break
            
	    #returning available chips
        print(f'\nTotal available value of chips: {chips.total}')
        
	    #setting up for playing again
        play_again = ''
        
        while play_again.lower() not in ['y', 'n']:
            play_again = input("\nDo you want to play again?\nEnter 'Y' for 'Yes' or 'N' for 'No'")
         
        
            if play_again.lower() == 'y':
                print("\nAlright, let's play again!")
                game_on = True
                break
            
            elif play_again.lower() == 'n':
                print("\nAlright, thank you for playing!")
                game_on = False
                break