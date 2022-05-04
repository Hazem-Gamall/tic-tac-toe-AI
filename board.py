
X = 1
O = 2

class Board:
    def __init__(self, human, computer) -> None:
        self.board = [
        [0,0,0],
        [0,0,0],
        [0,0,0] 
        ]

        self.human = human
        self.computer = computer

    def result(self, action):
        i, j, move = action

        if self.board[i][j] == 0:
            self.board[i][j] = move
        else:
            raise Exception("You can't play there")    

        if self.is_terminal():
            self.print_board()
            if self.check_draw():
                print("Draw!!!")
                exit()
            elif action[2] == self.computer:
                print("Computer Won")
                exit()
            else:
                print("You Won!")
                exit()


    def utility(self):
        if self.board[0][0] == self.computer and self.board[0][0] == self.board[0][1] and  self.board[0][0] == self.board[0][2]:
            return 10
        if self.board[1][0] == self.computer and self.board[1][0] == self.board[1][1] and  self.board[1][0] == self.board[1][2]:
            return 10
        if self.board[2][0] == self.computer and  self.board[2][0] == self.board[2][1] and  self.board[2][0] == self.board[2][2]:
            return 10
        if self.board[0][0] == self.computer and  self.board[0][0] == self.board[1][0] and  self.board[0][0] == self.board[2][0]:
            return 10
        if self.board[0][1] == self.computer and  self.board[0][1] == self.board[1][1] and  self.board[0][1] == self.board[2][1]:
            return 10
        if self.board[0][2] == self.computer and  self.board[0][2] == self.board[1][2] and  self.board[0][2] == self.board[2][2]:
            return 10
        if self.board[0][0] == self.computer and  self.board[0][0] == self.board[1][1] and  self.board[0][0] == self.board[2][2]:
            return 10
        if self.board[0][2] == self.computer and  self.board[0][2] == self.board[1][1] and  self.board[0][2] == self.board[2][0]:
            return 10
        elif self.check_draw():
            return 0
        else:
            return -10
        
    
    def is_terminal(self):
        if self.board[0][0] != 0 and self.board[0][0] == self.board[0][1] and  self.board[0][0] == self.board[0][2]:
            return True
        if self.board[1][0] != 0 and self.board[1][0] == self.board[1][1] and  self.board[1][0] == self.board[1][2]:
            return True
        if self.board[2][0] != 0 and  self.board[2][0] == self.board[2][1] and  self.board[2][0] == self.board[2][2]:
            return True
        if self.board[0][0] != 0 and  self.board[0][0] == self.board[1][0] and  self.board[0][0] == self.board[2][0]:
            return True
        if self.board[0][1] != 0 and  self.board[0][1] == self.board[1][1] and  self.board[0][1] == self.board[2][1]:
            return True
        if self.board[0][2] != 0 and  self.board[0][2] == self.board[1][2] and  self.board[0][2] == self.board[2][2]:
            return True
        if self.board[0][0] != 0 and  self.board[0][0] == self.board[1][1] and  self.board[0][0] == self.board[2][2]:
            return True
        if self.board[0][2] != 0 and  self.board[0][2] == self.board[1][1] and  self.board[0][2] == self.board[2][0]:
            return True
        else:
            return self.check_draw()

    def check_draw(self):
        for row in self.board:
            for element in row:
                if element == 0:
                    return False
        return True

    def actions(self, player):
        return [(i,j, player) for i in range(len(self.board)) for j in range(len(self.board[i])) if self.board[i][j] == 0]


    def print_board(self):
        for row in self.board:
            for element in row:
                # print("element:", element)
                print(('X' if element == X else 'O' if element == O else '_'), end='\t')
            print('')
        print('------------------\n')
