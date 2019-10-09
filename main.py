import random
import math
import operator
import copy
from game import game

ITERATIONS = 10000
# generate the number of iterations for each  available option
NUM_OPTIONS = int(math.floor(ITERATIONS/6))
# OBJECTS = [game() for i in range(NUM_OPTIONS)]
OBJECTS = game()
t_results = []
results = {
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}

if __name__ == "__main__":

    a_game = game()

    #game flux

    a_game.p_board()


    # make a test with same board
    # result = a_game.subgame(a_game.board, 12)
    # print(result)
    # a_game.reset()
    # print(a_game.board)

    while a_game.winner != 1:
        move_result = "NO EXTRA"
        #start the game with player 1 playing first
        if a_game.turn == 1:
            #get input of the move for the player
            print("Please Insert Move: " + str(a_game.valid_moves(1)))
            move = input()
            #send the move to the class
            move_result = a_game.make_move(1, int(move))
            #check if game ends
            if a_game.check_trigger_win() == 0:
                #sum all pebbles to mancalas
                a_game.end_game_sum()
                print("THE WINNER IS: " + str(a_game.determine_winner()))
                a_game.winner = 1
            #check if player 1 gets extra turn
            if move_result == "EXTRA TURN":
                a_game.turn = 1
            if move_result == "NO EXTRA":
                a_game.turn = 2
            a_game.p_board()
        if a_game.turn == 2:
            #get input of the move for the player
            print("Player 2 playing")
            if a_game.valid_moves(2):
                # LOGIC FOR MONTECARLO
                v_moves = a_game.valid_moves(2)
                # throw montecarlo for each valid move the player can do next
                for move in v_moves:
                    #do the number of iterations
                    for i in range(NUM_OPTIONS):
                        #throw a subgame for this boardstate
                        OBJECTS.subgame(copy.deepcopy(a_game.board), move)
                        #get the winner for this object
                        w_result = OBJECTS.determine_winner()
                        #add result to array
                        t_results.append(w_result)
                        #reset the object
                        OBJECTS.reset()

                    #get rid of all defeats from game
                    t1_results = list(filter(lambda a: a != 1, t_results))
                    #empty results
                    t_results = []
                    #get sum of score (its double but w/e)
                    results[move] = sum(t1_results)
                # select the best course for montecarlo
                move  = max(results.items(), key=operator.itemgetter(1))[0]

                # print(results)

                # no montecarlo
                # move = random.choice(a_game.valid_moves(2))

                #send the move to the class
                move_result = a_game.make_move(2, int(move))

            #reset for next montecarlo
            for index in results:
                results[index] = 0

            #check if game ends

            if a_game.check_trigger_win() == 0:
                #sum all pebbles to mancalas
                a_game.end_game_sum()
                print("THE WINNER IS: " + str(a_game.determine_winner()))
                a_game.winner = 1
            #check if player 2 gets extra turn
            if move_result == "EXTRA TURN":
                a_game.turn = 2
            if move_result == "NO EXTRA":
                a_game.turn = 1
            a_game.p_board()