import random
from game import game

if __name__ == "__main__":

    a_game = game()
    
    #game flux
    
    a_game.p_board()


    # make a test with same board
    result = a_game.subgame(a_game.board, 11)
    print(result)
    
    # while a_game.winner != 1:
    #     #start the game with player 1 playing first
    #     if a_game.turn == 1:
    #         #get input of the move for the player
    #         print("Please Insert Move: " + str(a_game.valid_moves(1)))
    #         move = input()
    #         #send the move to the class
    #         move_result = a_game.make_move(1, int(move))
    #         #check if game ends
    #         if a_game.check_trigger_win() == 0:
    #             #sum all pebbles to mancalas
    #             a_game.end_game_sum()
    #             print("THE WINNER IS: " + str(a_game.determine_winner()))
    #             a_game.winner = 1
    #         #check if player 1 gets extra turn
    #         if move_result == "EXTRA TURN":
    #             a_game.turn = 1
    #         if move_result == "NO EXTRA":
    #             a_game.turn = 2
    #         a_game.p_board()
    #     if a_game.turn == 2:
    #         #get input of the move for the player
    #         print("Player 2 playing")
    #         move  = random.choice(a_game.valid_moves(2))
    #         #send the move to the class
    #         move_result = a_game.make_move(2, int(move))
    #         #check if game ends
    #         if a_game.check_trigger_win() == 0:
    #             #sum all pebbles to mancalas
    #             a_game.end_game_sum()
    #             print("THE WINNER IS: " + str(a_game.determine_winner()))
    #             a_game.winner = 1
    #         #check if player 2 gets extra turn
    #         if move_result == "EXTRA TURN":
    #             a_game.turn = 2
    #         if move_result == "NO EXTRA":
    #             a_game.turn = 1
    #         a_game.p_board()