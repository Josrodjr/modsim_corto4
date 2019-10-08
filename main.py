import math
import random
#print(random.randint(0,5))

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
        
if __name__ == "__main__":

    a_game = game()
    
    #a_game.make_move(2, 11)
    #a_game.make_move(1, 4)
    #print(a_game.make_move(1, 3))
    #a = a_game.valid_moves(1)
    #print(a_game.determine_winner())
    #a_game.set_board([4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 1])
    #a_game.end_game_sum()

    #a_game.p_board()
    #print(a_game.check_trigger_win())
    
    #game flux
    
    a_game.p_board()
    
    while a_game.winner != 1:
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
            move  = random.choice(a_game.valid_moves(2))
            #send the move to the class
            move_result = a_game.make_move(2, int(move))
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
    
