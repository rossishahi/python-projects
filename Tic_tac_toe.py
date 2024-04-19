import random
import os
board = ['dummy',1,2,3,4,5,6,7,8,9]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset():
    board = ['dummy',1,2,3,4,5,6,7,8,9]
    return board

def board_out():

    global board
    
    print(f'\n{board[7]} | {board[8]} | {board[9]}')
    print('-'*9)
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('-'*9)
    print(f'{board[1]} | {board[2]} | {board[3]}')

def win_check(mark):
    global board

    if board[7]==board[8]==board[9]==mark or board[4]==board[5]==board[6]==mark or board[1]==board[2]==board[3]==mark or \
    board[7]==board[4]==board[1]==mark or board[8]==board[5]==board[2]==mark or board[9]==board[6]==board[3]==mark or \
    board[7]==board[5]==board[3]==mark or board[1]==board[5]==board[9]==mark:
        return True


def player_choice():
    option = ''
    pos = ['X', 'O']
    while option.lower() not in ['x', 'o']:
        option = input('Please enter your choice [X or O]')
    print(f'You have selected {option.upper()!r}')
    return option.upper()

def first_to_play(player_choice):
    
    option_1 = player_choice()
    
    if option_1 == 'X':
        option_2 = 'O'
    else:
        option_2 = 'X'

    play_first = random.choice([option_1, option_2]) 

    print(f'{play_first} will play first.')
    
    return play_first

def play(player_go, board_out, win_check):

    global board
    
    player_1 = player_go
    
    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
        
    count = 1
    game_won = False
    
    while count <= 9 and game_won == False:
        
        choice = ''
        
        while choice not in range(1,10) or not str(choice).isdigit():

            try: 
                if count % 2 == 0:
                    choice = int(input("\nPlayer 2: Please enter your position [1-9]."))
                else:
                    choice = int(input("\nPlayer 1: Please enter your position [1-9]."))
        
            except:
                print("Please enter only valid positions.")
                continue
        
            else:
                print(f'\nThis is turn number: {count}')
                clear_screen()

                if count % 2 == 0:
                    board[choice] = player_2
                    board_out()
                    
                    if win_check(player_2):
                        print(f'\nPlayer_2 with {player_2} has won!')
                        game_won = True
                        break
                else:
                    board[choice] = player_1
                    board_out()

                    if win_check(player_1):
                        print(f'\nPlayer_1 with {player_1} has won!')
                        game_won = True
                        break
                    
                count += 1
                continue
        
        



if __name__ == '__main__':
	
	while True:
		
		play_again = ''

		board = reset()
		player_go = first_to_play(player_choice)
		play(player_go, board_out, win_check)

		while play_again.lower() not in ['y', 'n']:
			play_again = input('\nDo you want to play again?: Y or N')
			if play_again.lower() == 'y':
				clear_screen()
				continue
			else:
				print("\nThank you for playing along.")
				break