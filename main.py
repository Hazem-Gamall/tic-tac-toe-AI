from tic_tac_toe import TicTacToe


def main():
    first = input("Choose X or O:")
    if first == 'X' or first == 'x':
        first = True
    elif first == 'O' or first == 'o':
        first = False
    else:
        print("Invalid Input try again")
        exit()
   
    print('Play by choosing your desired location according to the following:')
    print('7\t8\t9\n4\t5\t6\n1\t2\t3')
    print('Press Enter to continue...')
    input()
    game = TicTacToe(first)
    game.play()

main()