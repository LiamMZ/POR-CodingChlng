from abc import ABC, abstractmethod
import random


class AI(ABC):
    '''Abstract class'''
    @abstractmethod
    def play(self, game):
        pass

class RandomAI(AI):
    def play(self, game):
        '''An AI player that chooses a legal move at random out of all
        available legal moves in Tic-Tac-Toe state argument'''
        return random.choice(game.state.moves)
    
class AlphaBetaAI(AI):
    def play(self, game):
        '''An AI player the optimal legal move by
        the MiniMax algorithm with alpha beta pruning in a Tic-Tac-Toe game'''
        move = self.alphabeta_search(game)
        return move
    
    def alphabeta_search(self, game):
        '''search game approach to find best action, using alpha-beta pruning:
        alpha = best (highest) move found so far for Max
        beta  = best (lowest) move found so far for Min'''
        # Functions used by alphabeta
        def max_value(game,state,alpha,beta):
            #if termninal node return value and no move
            if game.game_over(state):
                return game.utility(state, game.state.to_move),None
            #initiallize worst case val
            value = -float('inf')
            bestMove = None #initialize best move
            #itterate over available moves
            for move in state.moves:
                #get result from the next node
                resp,_ = min_value(game,game.result(move,state),alpha,beta)
                #if the response was better than value
                #update value and best move
                if resp>value:
                    value = resp
                    bestMove = move
                #prune if value is greater than beta
                if value>=beta: return value,bestMove
                #update alpha
                alpha = max(alpha,value)
            return value,bestMove
        
        def min_value(game, state, alpha, beta):
            #if terminal node return value and no move
            if game.game_over(state):
                return game.utility(state, game.state.to_move),None
            #initialize value to worst case
            value = float('inf')
            #initialize best move var
            bestMove = None
            #itterate over available moves
            for move in state.moves:
                #get the response from max value
                resp,_ = max_value(game,game.result(move,state),alpha,beta)
                #if the response is less than val
                #update value and best move
                if resp<value:
                    value = resp
                    bestMove = move
                #if the value is less than or equal to alpha return
                if value<=alpha: return value,bestMove
                #update beta
                beta = min(beta,value)
            return value,bestMove
        
        # Body of alphabeta_cutoff_search:
        # player = game.state.to_move
        alpha = -float('inf')
        beta = float('inf')
        _,action = max_value(game,game.state,alpha,beta)
        return action

if __name__ == '__main__':
    ai1 = RandomAI()
    ai2 = AlphaBetaAI()