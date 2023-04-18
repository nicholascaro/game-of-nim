from games import *

class GameOfNim(Game):
    # takes the initial board position 
    # and creates the initial GameState. Note that a GameState 
    # includes all valid moves for that state.
     def __init__(self):
         pass
     
    # returns the new state reached from the given state 
    # and the given move. Assume the move is a valid move.
    # Note that the state for a multiplayer game also includes the 
    # player whose turn it is to play
     def result(state, move):
         pass
     
    # returns a list of valid actions in the given state. 
    # This is easy if you generate the list of valid moves 
    # when a child state is created.
     def actions(state):
         pass
     
    # returns True if the given state represents the end of a game
     def terminal_test(state):
         return True 
     
    # returns +1 if MAX wins, -1 if MIN wins (the "names" of the 
    # players don't matter as long as they are distinct)
     def utility(state, player):
         pass
     
    # returns the player whose turn it is to move. 
    # The default implementation in abstract class Game should be sufficient.
     def to_move(state):
         pass

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")