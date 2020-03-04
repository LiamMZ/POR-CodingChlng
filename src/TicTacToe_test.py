import unittest
from unittest.mock import patch
from TicTacToe import TicTacToe
from AI import AlphaBetaAI

class TicTacToeTest(unittest.TestCase):

    def testInitialMoves(self):
        '''Checks that the initial moves are correct'''
        game = TicTacToe()
        expected_moves = list((row,col) for row in range(1,4) for col in range(1,4))
        self.assertEqual(expected_moves, game.state.moves)
    
    def testResult(self):
        '''tests that game.result updates state.board correctly'''
        game = TicTacToe()
        state = game.result((1,1), game.state)
        expected_board = {(1,1):'X'}
        self.assertEqual(expected_board, state.board)
    
    def testComputeUtilityX_Row(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-x win)
        on a row wise win for X'''
        game = TicTacToe()
        game.state.board = {(1,1):'X', (1,2):'X'}
        utility = game.compute_utility((1,3), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)

    def testComputeUtilityX_Col(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-x win)
        on a Collumn-wise win for X'''
        game = TicTacToe()
        game.state.board = {(1,1):'X', (2,1):'X'}
        utility = game.compute_utility((3,1), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityX_LRDiag(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-x win)
        on a Left-Right Diagonal wise win for X'''
        game = TicTacToe()
        game.state.board = {(1,1):'X', (2,2):'X'}
        utility = game.compute_utility((3,3), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityX_RLDiag(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-x win)
        on a Right-Left Diagonal wise win for X'''
        game = TicTacToe()
        game.state.board = {(1,3):'X', (2,2):'X'}
        utility = game.compute_utility((3,1), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_Row(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a row wise win for O'''
        game = TicTacToe()
        game.state.board = {(1,1):'O', (1,2):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((1,3), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_Col(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a collumn wise win for O'''
        game = TicTacToe()
        game.state.board = {(1,1):'O', (2,1):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((3,1), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_LRDiag(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a Left-Right Diagonal wise win for O'''
        game = TicTacToe()
        game.state.board = {(1,1):'O', (2,2):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((3,3), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)

    def testComputeUtilityO_RLDiag(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a Right-Left Diagonal wise win for O'''
        game = TicTacToe()
        game.state.board = {(1,3):'O', (2,2):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((3,1), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testGameOver_Xwin(self):
        ''' tests that game over returns true
            when in a state with utility=1 (X win)'''
        game = TicTacToe()
        game.state.utility = 1
        check = game.game_over(game.state)
        self.assertEqual(check, True)

    def testGameOver_Owin(self):
        ''' tests that game over returns true
            when in a state with utility=-1 (O win)'''
        game = TicTacToe()
        game.state.utility = -1
        check = game.game_over(game.state)
        self.assertEqual(check, True)

    def test2PGame_Xwin(self):
        '''Runs a mock 2-player game wherer X should win'''
        mock = ['1 1',
                '1 2',
                '2 1',
                '1 3',
                '3 1']
        with patch('builtins.input', side_effect=mock):
            out = TicTacToe().play_2P_game()
        self.assertEqual(out, 'Player-X wins!')
    
    def test2PGame_Owin(self):
        '''Runs a mock 2-player game wherer O should win'''
        mock = ['1 1',
                '1 3',
                '2 1',
                '3 1',
                '3 3',
                '2 2']
        with patch('builtins.input', side_effect=mock):
            out = TicTacToe().play_2P_game()
        self.assertEqual(out, 'Player-O wins!')

if __name__=='__main__':
    unittest.main()