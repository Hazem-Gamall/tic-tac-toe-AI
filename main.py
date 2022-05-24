from tic_tac_toe import TicTacToe
from board import X, O, Board


def main():
    first = input("Choose X or O:")
    if first == 'X' or first == 'x':
        first = True
        board = Board(human = X, computer = O)
    elif first == 'O' or first == 'o':
        first = False
        board = Board(human = O, computer = X)
    else:
        print("Invalid Input try again")
        exit()
    print('Play by choosing your desired location according to the following:')
    print('7\t8\t9\n4\t5\t6\n1\t2\t3')
    print('Press Enter to continue...')
    input()
    game = TicTacToe(first, board)
    game.play()

main()