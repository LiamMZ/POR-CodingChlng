import copy as cp
from State import State

class TicTacToe:
    ''' Class with required functions for a TicTacToe game
    nrow = the number of rows for a game, default 3
    ncol = the number of columns for a game, default 3
    nwin = the number of marks in a row/column/diag to win, default 3'''
    def __init__(self, nrow=3, ncol=3, nwin=3):
        self.nrow = nrow
        self.ncol = ncol
        self.nwin = nwin
        moves = list((row, col) for row in range(1, nrow + 1) for col in range(1, ncol + 1))
        self.state = State(moves)

    def result(self, move, state):
        '''
        returns the hypothetical result of making move in state
        move  = (row, col) tuple where player will put their mark (X or O)
        state = a `State` object, to represent whose turn it is and form
                the basis for generating a **hypothetical** updated state
                that will result from making the given `move`
        This returns a **hypothetical** state, so that the alpha beta AI
        can check multiple outcomes without updating the actual game state
        '''
        # Don't do anything if the move isn't a legal one
        if move not in state.moves:
            return state
        # Return a copy of the updated state:
        new_state = cp.deepcopy(state)
        #compute utility
        new_state.utility = self.compute_utility(move, state)
        #update board with move
        new_state.board[move] = state.to_move
        #remove move from available moves
        new_state.moves.remove(move)
        #update turn
        new_state.to_move = ('O' if state.to_move == 'X' else 'X')
        return new_state

    def compute_utility(self, move, state):
        '''
        returns the utility of making move in state
        If 'X' wins with this move, return 1;
        if 'O' wins return -1;
        else return 0.
        '''        
        row, col = move
        player = state.to_move
        
        # create a hypothetical copy of the board, with 'move' executed
        board = cp.deepcopy(state.board)
        board[move] = player
        
        # check for row-wise win
        in_a_row = 0
        for c in range(1,self.ncol+1):
            in_a_row += board.get((row,c))==player

        # check for column-wise win
        in_a_col = 0
        for r in range(1,self.nrow+1):
            in_a_col += board.get((r,col))==player

        # check for Upper Left-> Lower Right diagonal win
        in_a_diag1 = 0
        for r in range(row,0,-1):
            in_a_diag1 += board.get((r,col-(row-r)))==player
        for r in range(row+1,self.nrow+1):
            in_a_diag1 += board.get((r,col-(row-r)))==player

        #check for Upper Right-> Lower Left diagonal win
        in_a_diag2 = 0
        for r in range(row,0,-1):
            in_a_diag2 += board.get((r,col+(row-r)))==player
        for r in range(row+1,self.nrow+1):
            in_a_diag2 += board.get((r,col+(row-r)))==player
        
        if self.nwin in [in_a_row, in_a_col, in_a_diag1, in_a_diag2]:
            return 1 if player=='X' else -1
        else:
            return 0

    def game_over(self, state):
        '''game is over if someone has won (utility!=0) or there
        are no more moves left'''
        return state.utility!=0 or len(state.moves)==0    

    def utility(self, state, player):
        '''Return the value to player; 1 for win, -1 for loss, 0 otherwise.'''
        return state.utility if player=='X' else -state.utility

    def display(self):
        '''display board in console with row/col indicies'''
        board = self.state.board
        print("Board:")
        print(' ', end=' ')
        #print column indicies
        for col in range(1, self.ncol + 1):
            print(col, end=' ')
        print() 
        for row in range(1, self.nrow + 1):
            #print row indicies
            print(row, end=' ')
            #print board entries or . if there is no mark in space
            for col in range(1, self.ncol + 1):
                print(board.get((row, col), '.'), end=' ')
            print()

    def validate_input(self, user_input):
        try:
            move = (int(user_input.split()[0]),
                    int(user_input.split()[1]))
        except (ValueError, KeyError):
            #force key error if invlaid entry
            move = (int(user_input.split()[2]),
                    int(user_input.split()[1]))
        #check if more than two arguments are given
        if len(user_input.split())>2:
            raise ValueError('Too many arguments given')
        #check for out of bounds move
        if (move[0]<0 or move[1]<0) or(move[0]>self.nrow or move[1]>self.ncol):
            raise ValueError('Out of Bounds Move')
        #check if move is already taken
        if(move in self.state.board):
            raise ValueError('Move Already Taken')

        return move

    def handle_input(self):
        '''Method to handle user input for a game'''
        while True:
            #show updated board and request user move
            self.display()
            print ('Player-{} please enter the row and column for your move separated by a space'
            .format(self.state.to_move))
            try:
                #try to read in user input
                input_coords = input()
                move = self.validate_input(input_coords)
            #if input is invalid loop until valid input is recieved
            except(ValueError, IndexError, KeyError):
                print('\nThe coordinates you entered are invalid please enter valid coordinates.\n')
                continue
            break
        return move
    
    def play_1P_game(self, player2):
        '''Play a game of tic-tac-toe vs an AI'''
        turn_limit = self.nrow*self.ncol  # limit in case of buggy code
        turn = 0
        while turn<=turn_limit:
            for i in range(1,3):
                turn += 1
                #user turn
                if i==1:
                    move = self.handle_input()
                #AI turn
                else:
                    move = player2(self)
                #update state with selected move
                self.state = self.result(move, self.state)
                #check for game over
                if self.game_over(self.state):
                    #display final board
                    self.display()
                    #check if there is a winner or draw
                    if self.state.utility==0:
                        return 'The game ends in a draw!'
                    return 'Player-{} wins!'.format('X' if self.state.to_move=='O' else 'O')
    
    def play_2P_game(self):
        '''Play a game of tic tac toe with 2 human players'''
        turn_limit = self.nrow*self.ncol  # limit in case of buggy code
        turn = 0
        while turn<=turn_limit:
            for _ in range(2):
                turn+=1
                move = self.handle_input()
                #update state with selected move
                self.state = self.result(move, self.state)
                #check for game over
                if self.game_over(self.state):
                    #display final board
                    self.display()
                    #check for winner or draw
                    if self.state.utility==0:
                        return 'The game ends in a draw!'
                    return 'Player-{} wins!'.format('X' if self.state.to_move=='O' else 'O')

     
if __name__ == '__main__':
    game = TicTacToe()
    print(game.play_2P_game())
