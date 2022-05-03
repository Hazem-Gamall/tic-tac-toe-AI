import math
from board import X, O, Board

class TicTacToe:
    def __init__(self, first:bool) -> None:
        self.first = first

        if first:
            self.human = X
            self.computer = O
        else:
            self.human = O
            self.computer = X
    
        self.board = Board(self.human, self.computer)


    

    def max_val(self):
        if self.board.is_terminal():
            # print(utility(state, X))
            return self.board.utility()
        value = -math.inf
        for action in self.board.actions(self.computer):
            self.board.board[action[0]][action[1]] = action[2]
            value = max(value, self.min_val())
            self.board.board[action[0]][action[1]] = 0

        return value

    def min_val(self):
        if self.board.is_terminal():
            # print(utility(state, O))
            return self.board.utility()
        value = math.inf
        for action in self.board.actions(self.human):
            self.board.board[action[0]][action[1]] = action[2]
            value = min(value, self.max_val())
            self.board.board[action[0]][action[1]] = 0

        return value


    def minimax(self): 
        value = self.min_val()
        return value



    def best_move(self):
        allowed_moves = self.board.actions(self.computer)
        best_score = -math.inf
        best_move = ()
        for move in allowed_moves:
            self.board.board[move[0]][move[1]] = self.computer
            score = self.minimax()
            self.board.board[move[0]][move[1]] = 0
            # print(move, score)
            if score > best_score:
                best_score = score
                best_move = move
        self.board.result(best_move)

    def getInput(self):
        numpad_move_lookup={
            1:[2,0],
            2:[2,1],
            3:[2,2],
            4:[1,0],
            5:[1,1],
            6:[1,2],
            7:[0,0],
            8:[0,1],
            9:[0,2]
        }
        user_input = int(input("where to?:"))
        if user_input > 9 or user_input < 1:
            raise Exception("invalid number")
        move = numpad_move_lookup[user_input]
        move.append(self.human)
        return move


    def play(self):
        while not self.board.is_terminal():
            try:
                if self.first:                    
                    self.board.result(self.getInput())
                    self.board.print_board()  

                    self.best_move()  
                    self.board.print_board()

                else:
                    self.best_move()  
                    self.board.print_board()

                    self.board.result(self.getInput())
                    self.board.print_board()  


            except Exception as e:

                self.board.print_board()
                print(e)
                continue

            

        
