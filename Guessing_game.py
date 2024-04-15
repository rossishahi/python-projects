import random

def intro():
    print("Hi,\nWelcome to this Guessing Game!")
    name = input("\nPlease enter your name!")
    print(f'\nHello, {name}!')

def instructions():
    print("\nPlease note the following instructions before we start.")
    print("\nInstructions:")
    print("1. I have picked a random number between 1 to 100 (limits inclusive). You have to guess that number to win.")
    print("2. If your guess is within 10 of the number, I'll say 'WARM!'. Otherwise, I'll say 'COLD!'")
    print("3. On subsequent guesses, I'll let you know if you are closer or farther when compared to your previous guess.\nI'll use 'WARMER!' or 'COLDER!' respectively.")
    print("\nHope this is clear to you. Now, let us start.")

def random_value():
    to_guess = random.randint(1,100)
    print("\nI have picked a number!")
    return to_guess

def game_on(random_value):
    
    to_guess = random_value()

    player_guesses = []
    
    game_won = False
    
    while not game_won:
        
        player_input = ''
            
        while player_input not in range(1,101) or str(player_input).isdigit() == False:
    
            
            try:
                player_input = int(input("\nPlease enter a valid guess from 1 to 100."))
                
                if player_input not in range(1,101):
                    print("Sorry, the entry is out of bounds.")
    
            except:
                print("Entered value is inappropriate.")
                continue
                
            else:
                   
                if player_input in range(1,100) and str(player_input).isdigit():
    
                    player_guesses.append(player_input)
    
                    if player_input == to_guess:
                        print(f"Congratulations, you have guessed correctly in {len(player_guesses)} attempts.")
                        game_won = True
                        break
        
                            
                    elif player_input != to_guess and len(player_guesses) > 1:
        
                        if abs(to_guess - player_guesses[-2]) < abs(to_guess - player_input):
                            print("COLDER!")
                        else:
                            print("WARMER!")
                        continue
                    
                    elif player_input != to_guess and len(player_guesses) == 1: 
        
                        if abs(to_guess - player_input) <= 10:
                            print("WARM!")
                        else:
                            print("COLD!")
                        continue


if __name__ =='__main__':
    intro()
    instructions()
    game_on(random_value)