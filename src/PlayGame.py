import numpy as np
from TicTacToe import TicTacToe
from AI import RandomAI
from AI import AlphaBetaAI

def handleMenuInput(input):
    if input not in [1,2]:
        raise ValueError
    return True

def play():
    while True:
        print('Welcome to Tic-Tac-Toe! Please enter an option Below:')
        print('1 - Play solo against an AI')
        print('2 - Play a 2 player game against a friend')
        try:
            option = int(input())
            _ = handleMenuInput(option)
        except (ValueError):
            print('The option you entered is invalide please enter valid option.')
            continue
        break
    
    game = TicTacToe()
    if option == 1:
        while True:
            print('Please enter an option below:')
            print('1 - Easy AI')
            print('2 - Hard AI (Warning the hard AI takes longer to decide)')
            try:
                choice = int(input())
                _ = handleMenuInput(choice)
            except (ValueError):
                print('The option you entered is invalid please enter valid option.')
                continue
            break
        if choice == 1:
            game.play_1P_game(RandomAI().play)
        else:
            game.play_1P_game(AlphaBetaAI().play)
    else:
        print(game.play_2P_game())

if __name__=='__main__':
    play()