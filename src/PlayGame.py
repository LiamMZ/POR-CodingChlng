from TicTacToe import TicTacToe
from AI import RandomAI
from AI import AlphaBetaAI

def handleMenuInput(input):
    '''Function to check for valid input'''
    if input not in [1,2]:
        raise ValueError
    return True

def play():
    '''Function that runs a tic tac toe game
    Can either play vs an AI or against another human'''
    #Request user input for game type
    while True:
        print('Welcome to Tic-Tac-Toe! Please enter an option Below:')
        print('1 - Play solo against an AI')
        print('2 - Play a 2 player game against a friend')
        try:
            option = int(input())
            _ = handleMenuInput(option)
        #if input invalid loop until valid input recieved
        except (ValueError):
            print('The option you entered is invalide please enter valid option.')
            continue
        break
    #instantiate tic tac toe functions
    game = TicTacToe()
    #If option = 1 request AI preference
    if option == 1:
        #request user input for AI type
        while True:
            print('Please enter an option below:')
            print('1 - Easy AI')
            print('2 - Hard AI (Warning the hard AI takes longer to decide)')
            try:
                choice = int(input())
                _ = handleMenuInput(choice)
            #if input invalid loop until valid input recieved
            except (ValueError):
                print('The option you entered is invalid please enter valid option.')
                continue
            break
        #if choice = 1 run a game with random ai
        if choice == 1:
            print(game.play_1P_game(RandomAI().play))
        #if choice = 2 run a game with alpha beta ai
        else:
            print(game.play_1P_game(AlphaBetaAI().play))
    #If option = 2 run a 2-Player game
    else:
        print(game.play_2P_game())

if __name__=='__main__':
    play()