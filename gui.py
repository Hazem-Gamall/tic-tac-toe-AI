from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont

from tic_tac_toe import TicTacToe
from board import Board, X, O

font = ('Helvetica',36)


def create_main_window():
    global root
    root = Tk()
    root.geometry('400x400')
    root.title('Tic Tac Toe')
    root.resizable(0,0)

    root.columnconfigure(0,weight=1)
    root.rowconfigure(0, weight= 1)





def create_frame():

    ttk.Style().configure('TFrame', background='black')

    mainframe = ttk.Frame(root)
    mainframe.grid(row=0, column=0, padx=10, pady=10, sticky=(S,N,W,E))

    #tell tkinter that i have 3 equal columns and 3 equal rows
    mainframe.columnconfigure(0,weight=1)
    mainframe.columnconfigure(1,weight=1)
    mainframe.columnconfigure(2,weight=1)

    mainframe.rowconfigure(0, weight=1)
    mainframe.rowconfigure(1, weight=1)
    mainframe.rowconfigure(2, weight=1)

    global board_buttons 
    board_buttons = []

    #create the ui representation of the board as a grid of buttons
    for i in range(3):
        temp_list = []
        for j in range(3):
            button = Button(mainframe, relief='flat', font=font, width=1,command=lambda i = i, j = j: make_move(i,j))
            button.grid(row=i,column=j, padx=1, pady=1, sticky=(N,W,E,S))
            temp_list.append(button)
        board_buttons.append(temp_list)




def restart_game(window):
    board.reset()
    for row in board_buttons:
        for button in row:
            button['text'] = ''
    root.destroy()
    main()
    

def create_subwindow(label_text, independent:bool = False):
    subwindow = Tk() if independent else Toplevel(root)
    subwindow.title('Alert')
    ttk.Label(subwindow, text=label_text, font=font).grid(row=0, column=0, sticky=(N,W,E,S),padx=10,pady=10)
    Button(subwindow, text='Restart', border=2, command=lambda: restart_game(subwindow)).grid(row=1, column=0, pady=10, sticky=W)
    Button(subwindow, text='Close', border=2, command=subwindow.destroy).grid(row=1, column=1, pady=10, sticky=E)
    return subwindow


def check_game_state(player) -> bool:
    if board.is_terminal():
        board.print_board()
        message = ''
        if board.check_draw():
            print("Draw!!!")
            message = 'Draw'
        elif player == board.computer:
            print("Computer Won")
            message = 'Computer Won'
        else:
            print("You Won!")
            message = 'You won'
        create_subwindow(message)
        return True


def make_move(i, j):
    if not board.is_terminal():
        print(i,j)
        board.print_board()
        try:
            board.result((i, j, human))
            board_buttons[i][j]['text'] = 'X' if human == X else 'O'
            if check_game_state(human):
                return  #the game is over, leave the function and don't perform to the computer's move
            ai_move = tic_tac_toe_AI.best_move()
            print(ai_move)
            if ai_move:
                board_buttons[ai_move[0]][ai_move[1]]['text'] = 'X' if computer == X else 'O'
            check_game_state(computer)
        except Exception as e:
            create_subwindow(e)
            print(e)



def ai_first_move():
    w = create_subwindow('Loading...')
    move = []
    thread = Thread(target=lambda: move.append(tic_tac_toe_AI.best_move()))
    thread.start()
    root.withdraw()
    w.update()
    thread.join() 
    root.deiconify()
    move = move[0]
    w.destroy()
    board_buttons[move[0]][move[1]]['text'] = 'X'


def main():
    window = Tk()
    global board, tic_tac_toe_AI
    selection = IntVar()
    Radiobutton(window, text='X',font=font, variable=selection, value=X, command=window.destroy).grid(row=0,column=0)
    Radiobutton(window, text='O',font=font, variable=selection, value=O,command=window.destroy).grid(row=0,column=1)
    window.mainloop()
    global human, computer, first
    
    create_main_window()
    create_frame()

    if selection.get() == X:
        human, computer, first  = X, O, True
    else:
        human, computer, first  = O, X, False

    board = Board(human,computer)
    tic_tac_toe_AI = TicTacToe(first, board)
    if computer == X:
        ai_first_move()

    root.mainloop()

main()