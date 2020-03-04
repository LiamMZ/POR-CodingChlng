# POR-CodingChlng
Coding Challenge for POR

Tic Tac Toe
=========================== 
This is a tic-tac-toe command line game that you can play 1-Player against 2 different AI options or 2-Player against another human.

## Code Details
### Board
  1 2 3
1 . . .
2 . . .
3 . . .
Above is an example of the game board shown in command line. The default board is 3x3 with a starting index of 1.
## Players
For the 1-Player mode the human is automatically the first player, with game marker **X**.
### AI
#### Easy (Random) AI
This AI will randomly choose from the available moves on their turn.

#### Hard (Alpha Beta) AI
This AI will choose the optimal move based on the [mini-max algorithm](https://en.wikipedia.org/wiki/Minimax) using the [alpha beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) method.

## How To Run

|        Command          | Runs |
| -------------------- | ---------- |
| python3 /src/PlayGame.py  |          A Game of Tic Tac Toe |
| python3 /src/TicTacToe_test.py   |         Unit Tests |


