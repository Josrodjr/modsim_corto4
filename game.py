import math
import random

class game:
    #game board
    board = []
    #current turn 1 or 2
    turn = 1
    #game status 0 incomplete 1 finished
    status = 0
    #winner 1 or 2
    winner = 0

    def __init__(self):
        self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    def p_board(self):
        upper_row = ""
        lower_row = ""
        i = 12
        j = 0
        #imprimir decreciente jugador 2
        while i >= 7:
            upper_row = upper_row + " " + str(self.board[i])
            i -= 1

        #imprimir en orden creciente el jugador 1
        while j <= 5:
            lower_row = lower_row + " " + str(self.board[j])
            j += 1

        print(upper_row)
        print(str(self.board[13])+"           "+str(self.board[6]))
        print(lower_row)

    def check_trigger_win(self):
        p2_board = self.board[7:13]
        p1_board = self.board[0:6]
        if sum(p2_board) == 0:
            return 0
        if sum(p1_board) == 0:
            return 0
        return 1

    def make_move(self, player, throw):
        #get the number of pebbles on throw
        pebbles = self.board[throw]
        #empty the cup we grabbed
        self.board[throw] = 0
        #move the pebbles except of the last one
        while pebbles > 0:
            #logic for throw of player 1
            if player == 1:
                next_spot = throw + 1
                #skip enemy mancala
                if next_spot == 13:
                    throw = next_spot
                else:
                    if next_spot > 13:
                        next_spot = next_spot % 14
                    self.board[next_spot] += 1
                    pebbles -= 1
                    throw = next_spot
                if pebbles == 0:
                    #cuando cae en un lugar vacio
                    if self.board[throw] == 1:
                        #formula para mirror 6-lugar que cayo + 6 = mirror
                        mirror =  (6 - throw) + 6
                        #pasar el mancala actual y el enemigo a nuestro mancala porque gratis
                        self.board[6] += self.board[throw]
                        self.board[throw] = 0
                        self.board[6] += self.board[mirror]
                        self.board[mirror] = 0
                    #si cayo en mancala de jugador
                    if throw == 6:
                        return "EXTRA TURN"
                    return "NO EXTRA"



            #logic for throw player 2
            if player == 2:
                next_spot = throw + 1
                #skip enemy mancala
                if next_spot == 6:
                    throw = next_spot
                else:
                    if next_spot > 13:
                        next_spot = next_spot % 14
                    self.board[next_spot] += 1
                    pebbles -= 1
                    throw = next_spot
                if pebbles == 0:
                    #si cayo en mancala de jugador
                    if throw == 13:
                        return "EXTRA TURN"
                    return "NO EXTRA"

    def valid_moves(self, player):
        valid_indexes = []
        if player == 1:
            i = 5
            while i >= 0:
                #check if there is something in the spot
                if self.board[i] != 0:
                    valid_indexes.append(i)
                i -= 1
        if player == 2:
            i = 7
            while i <= 12:
                #check if there is something in the spot
                if self.board[i] != 0:
                    valid_indexes.append(i)
                i += 1
        return valid_indexes

    def determine_winner(self):
        p1_mancala = self.board[6]
        p2_mancala = self.board[13]
        if p1_mancala > p2_mancala:
            return 1
        elif p2_mancala > p1_mancala:
            return 2
        else:
            return 0

    def set_board(self, board):
        self.board = board

    def end_game_sum(self):
        i = 5
        while i >= 0:
            # sum spot to player 1 mancala
            self.board[6] += self.board[i]
            self.board[i] = 0
            i -= 1
        i = 7
        while i <= 12:
            #sum spot to player 2 mancala
            self.board[13] += self.board[i]
            self.board[i] = 0
            i += 1
        return 0

    def subgame(self, boardstate, firstmove):
        #set this board game as subgame
        self.set_board(boardstate)
        #try and maximize 2 player 2 starts.
        self.turn = 2
        result = self.make_move(self.turn, firstmove)
        if result == "EXTRA TURN":
            #throw again
            move  = random.choice(self.valid_moves(2))
            self.make_move(self.turn, move)
        #else start infinite loop
        self.turn = 1
        while self.winner != 1:
            #start the game with player 1 playing first
            move_result = "NO EXTRA"
            if self.turn == 1:
                # print("Player 1 playing")
                #get input of the move for the player
                if self.valid_moves(1):
                    move  = random.choice(self.valid_moves(1))
                    #send the move to the class
                    move_result = self.make_move(1, int(move))
                #check if game ends
                if self.check_trigger_win() == 0:
                    #sum all pebbles to mancalas
                    self.end_game_sum()
                    # print("THE WINNER IS: " + str(self.determine_winner()))
                    self.winner = 1
                #check if player 1 gets extra turn
                if move_result == "EXTRA TURN":
                    self.turn = 1
                if move_result == "NO EXTRA":
                    self.turn = 2

            if self.turn == 2:
                #get input of the move for the player
                # print("Player 2 playing")
                if self.valid_moves(2):
                    move  = random.choice(self.valid_moves(2))
                    #send the move to the class
                    move_result = self.make_move(2, int(move))
                #check if game ends
                if self.check_trigger_win() == 0:
                    #sum all pebbles to mancalas
                    self.end_game_sum()
                    # print("THE WINNER IS: " + str(self.determine_winner()))
                    self.winner = 1
                #check if player 2 gets extra turn
                if move_result == "EXTRA TURN":
                    self.turn = 2
                if move_result == "NO EXTRA":
                    self.turn = 1
        #return if win or loose
        return self.board

    def reset(self):
        #game board
        self.board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        #current turn 1 or 2
        self.turn = 1
        #game status 0 incomplete 1 finished
        self.status = 0
        #winner 1 or 2
        self.winner = 0