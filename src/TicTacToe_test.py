import unittest
import io
import sys
from unittest.mock import patch
from TicTacToe import TicTacToe
from AI import AlphaBetaAI,RandomAI

class TicTacToeTest(unittest.TestCase):

    def testInitialMoves(self):
        '''Tests that all moves are available on instantiation'''
        game = TicTacToe()
        expected_moves = list((row,col) for row in range(1,4) for col in range(1,4))
        self.assertEqual(expected_moves, game.state.moves)
    
    def testResult(self):
        '''Tests that game.result updates state.board correctly'''
        game = TicTacToe()
        state = game.result((1,1), game.state)
        expected_board = {(1,1):'X'}
        self.assertEqual(expected_board, state.board)
    
    def testComputeUtilityX_Row1(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-X win)
        on a row-wise win for X in row 1'''
        game = TicTacToe()
        game.state.board = {(1,1):'X', (1,2):'X'}
        utility = game.compute_utility((1,3), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityX_Row2(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-X win)
        on a row-wise win for X in row 2'''
        game = TicTacToe()
        game.state.board = {(2,1):'X', (2,2):'X'}
        utility = game.compute_utility((2,3), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityX_Row3(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-X win)
        on a row-wise win for X in row 3'''
        game = TicTacToe()
        game.state.board = {(3,1):'X', (3,2):'X'}
        utility = game.compute_utility((3,3), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)

    def testComputeUtilityX_Col1(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-X win)
        on a column-wise win for X in column 1'''
        game = TicTacToe()
        game.state.board = {(1,1):'X', (2,1):'X'}
        utility = game.compute_utility((3,1), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)

    def testComputeUtilityX_Col2(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-X win)
        on a column-wise win for X in column 2'''
        game = TicTacToe()
        game.state.board = {(1,2):'X', (2,2):'X'}
        utility = game.compute_utility((3,2), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityX_Col3(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-X win)
        on a column-wise win for X in column 3'''
        game = TicTacToe()
        game.state.board = {(1,3):'X', (2,3):'X'}
        utility = game.compute_utility((3,3), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityX_LRDiag(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-X win)
        on a Left-Right-Diagonal-wise win for X'''
        game = TicTacToe()
        game.state.board = {(1,1):'X', (2,2):'X'}
        utility = game.compute_utility((3,3), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityX_RLDiag(self):
        '''Tests that game.compute_utility returns a utility of 1(Player-X win)
        on a Right-Left-Diagonal-wise win for X'''
        game = TicTacToe()
        game.state.board = {(1,3):'X', (2,2):'X'}
        utility = game.compute_utility((3,1), game.state)
        expected_utility = 1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_Row1(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a row-wise win for O in row 1'''
        game = TicTacToe()
        game.state.board = {(1,1):'O', (1,2):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((1,3), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_Row2(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a row-wise win for O in row 2'''
        game = TicTacToe()
        game.state.board = {(2,1):'O', (2,2):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((2,3), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_Row3(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a row-wise win for O in row 3'''
        game = TicTacToe()
        game.state.board = {(3,1):'O', (3,2):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((3,3), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_Col1(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a column-wise win for O in column 1'''
        game = TicTacToe()
        game.state.board = {(1,1):'O', (2,1):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((3,1), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_Col2(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a column-wise win for O in column 2'''
        game = TicTacToe()
        game.state.board = {(1,2):'O', (2,2):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((3,2), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_Col3(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a column-wise win for O in column 3'''
        game = TicTacToe()
        game.state.board = {(1,3):'O', (2,3):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((3,3), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)
    
    def testComputeUtilityO_LRDiag(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a Left-Right-Diagonal-wise win for O'''
        game = TicTacToe()
        game.state.board = {(1,1):'O', (2,2):'O'}
        game.state.to_move = 'O'
        utility = game.compute_utility((3,3), game.state)
        expected_utility = -1
        self.assertEqual(utility,expected_utility)

    def testComputeUtilityO_RLDiag(self):
        '''Tests that game.compute_utility returns a utility of -1(Player-O win)
        on a Right-Left-Diagonal-wise win for O'''
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
    
    def testGameOver_NoWin(self):
        ''' tests that game over returns False
            when in a state with utility=0 (No win)'''
        game = TicTacToe()
        game.state.utility = 0
        check = game.game_over(game.state)
        self.assertEqual(check, False)

    def test2PGame_Xwin(self):
        '''Runs a mock 2-player game where X should win'''
        #mock user input
        mock = ['1 1', #X
                '1 2', #O
                '2 1', #X
                '1 3', #O
                '3 1'] #X
        #suppress game print output
        text_trap = io.StringIO()
        sys.stdout = text_trap
        with patch('builtins.input', side_effect=mock):
            out = TicTacToe().play_2P_game()
        sys.stdout = sys.__stdout__
        self.assertEqual(out, 'Player-X wins!')
    
    def test2PGame_Owin(self):
        '''Runs a mock 2-player game where O should win'''
        #mock user input
        mock = ['1 1',
                '1 3',
                '2 1',
                '3 1',
                '3 3',
                '2 2']
        #suppress game print output
        text_trap = io.StringIO()
        sys.stdout = text_trap
        with patch('builtins.input', side_effect=mock):
            out = TicTacToe().play_2P_game()
        sys.stdout = sys.__stdout__
        self.assertEqual(out, 'Player-O wins!')

    def test2PGame_Draw(self):
        '''Runs a mock 2-player game that should end in a draw'''
        #mock user input
        mock = ['1 1',#X
                '1 2',#O
                '1 3',#X
                '3 3',#O
                '3 2',#X
                '3 1',#O
                '2 1',#X
                '2 2',#O
                '2 3']#X
        #suppress game print output
        text_trap = io.StringIO()
        sys.stdout = text_trap
        with patch('builtins.input', side_effect=mock):
            out = TicTacToe().play_2P_game()
        sys.stdout = sys.__stdout__
        self.assertEqual(out, 'The game ends in a draw!')

    def test2PGame_Xwin_InvalidInput(self):
        '''Runs a mock 2-player game where Player-X inputs invalid
        coordinates but eventually inputs correct coordinates
        Player-X should win'''
        #mock user input
        mock = ['a 18',
                '. 2',
                '45 .',
                '1 @',
                '1 1',
                '1 2',
                '2 1',
                '1 3',
                '3 1']
        #suppress game print output
        text_trap = io.StringIO()
        sys.stdout = text_trap
        with patch('builtins.input', side_effect=mock):
            out = TicTacToe().play_2P_game()
        sys.stdout = sys.__stdout__
        self.assertEqual(out, 'Player-X wins!')

    def test2PGame_Owin_invalidInput(self):
        '''Runs a mock 2-player game where Player-O inputs invalid
        coordinates but eventually inputs correct coordinates
        Player-O should win'''
        #mock user input
        mock = ['1 1',
                'a 18',
                '. 2',
                '45 .',
                '1 @',
                '1 3',
                '2 1',
                '3 1',
                '3 3',
                '2 2']
        #suppress game print output
        text_trap = io.StringIO()
        sys.stdout = text_trap
        with patch('builtins.input', side_effect=mock):
            out = TicTacToe().play_2P_game()
        sys.stdout = sys.__stdout__
        self.assertEqual(out, 'Player-O wins!')

    def testRandomAI(self):
        '''Tests that the random AI returns a move
        within the available moves'''
        ai = RandomAI()
        game = TicTacToe()
        move = ai.play(game)
        self.assertIn(move, game.state.moves)
    
    def testRandomAI_oneMove(self):
        '''Tests that the random AI returns a move
        within the available moves when only one move is available'''
        ai = RandomAI()
        game = TicTacToe()
        game.state.moves = [(1,1)]
        move = ai.play(game)
        self.assertIn(move, game.state.moves)

    def testAlphaBetaAI(self):
        '''Tests that the Alpha Beta AI returns a move
        within the available moves'''
        ai = AlphaBetaAI()
        game = TicTacToe()
        print('Waiting for Alpha_Beta AI to choose Move...')
        move = ai.play(game)
        self.assertIn(move, game.state.moves)

    def testAlphaBetaAI_oneMove(self):
        '''Tests that the Alpha beta AI returns a move
        within the available moves when only one move is available'''
        ai = AlphaBetaAI()
        game = TicTacToe()
        game.state.moves = [(1,1)]
        print('Waiting for Alpha_Beta AI to choose Move...')
        move = ai.play(game)
        self.assertIn(move, game.state.moves)

if __name__=='__main__':
    unittest.main()