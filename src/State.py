class State:
    '''Class to hold the state of a TicTacToe game
        to_move = the player whose turn it is
        utility = the value of a state, 0 for no winner,
                    1 for X win, -1 for O winn
        board = current spots on the board that have been marked
        moves = available moves'''
    def __init__(self, moves):
        self.to_move = 'X'
        self.utility = 0
        self.board = {}
        self.moves = moves