
import math
from tic_tac_toe import TicTacToe

# X = 1
# O = 2

# computer = O
# human = X
# def result(state, action):

#     i, j, move = action

#     if state[i][j] == 0:
#         state[i][j] = move
#         if is_terminal(state):
#             print_state(state)
#             if check_draw(state):
#                 print("Draw!!!")
#                 exit()
#             elif action[2] == computer:
#                 print("Computer Won")
#                 exit()
#             else:
#                 print("You Won!")
#                 exit()
#     else:
#         raise Exception("You can't play there")    
    
   
    
# def utility(state):
#     if state[0][0] == computer and state[0][0] == state[0][1] and  state[0][0] == state[0][2]:
#         return 10
#     if state[1][0] == computer and state[1][0] == state[1][1] and  state[1][0] == state[1][2]:
#         return 10
#     if state[2][0] == computer and  state[2][0] == state[2][1] and  state[2][0] == state[2][2]:
#         return 10
#     if state[0][0] == computer and  state[0][0] == state[1][0] and  state[0][0] == state[2][0]:
#         return 10
#     if state[0][1] == computer and  state[0][1] == state[1][1] and  state[0][1] == state[2][1]:
#         return 10
#     if state[0][2] == computer and  state[0][2] == state[1][2] and  state[0][2] == state[2][2]:
#         return 10
#     if state[0][0] == computer and  state[0][0] == state[1][1] and  state[0][0] == state[2][2]:
#         return 10
#     if state[0][2] == computer and  state[0][2] == state[1][1] and  state[0][2] == state[2][0]:
#         return 10
#     elif check_draw(state):
#         return 0
#     else:
#         return -10
    
  
# def is_terminal(state):
#     if state[0][0] != 0 and state[0][0] == state[0][1] and  state[0][0] == state[0][2]:
#         return True
#     if state[1][0] != 0 and state[1][0] == state[1][1] and  state[1][0] == state[1][2]:
#         return True
#     if state[2][0] != 0 and  state[2][0] == state[2][1] and  state[2][0] == state[2][2]:
#         return True
#     if state[0][0] != 0 and  state[0][0] == state[1][0] and  state[0][0] == state[2][0]:
#         return True
#     if state[0][1] != 0 and  state[0][1] == state[1][1] and  state[0][1] == state[2][1]:
#         return True
#     if state[0][2] != 0 and  state[0][2] == state[1][2] and  state[0][2] == state[2][2]:
#         return True
#     if state[0][0] != 0 and  state[0][0] == state[1][1] and  state[0][0] == state[2][2]:
#         return True
#     if state[0][2] != 0 and  state[0][2] == state[1][1] and  state[0][2] == state[2][0]:
#         return True
#     else:
#         return check_draw(state)



# def check_draw(state):
#     for row in state:
#         for element in row:
#             if element == 0:
#                 return False
#     return True
    
# def actions(state, player):
#     return [(i,j, player) for i in range(len(state)) for j in range(len(state[i])) if state[i][j] == 0]

# def max_val(state):
#     if is_terminal(state):
#         # print(utility(state, X))
#         return utility(state)
#     value = -math.inf
#     for action in actions(state, computer):
#         state[action[0]][action[1]] = action[2]
#         value = max(value, min_val(state))
#         state[action[0]][action[1]] = 0

#     return value

# def min_val(state):
#     if is_terminal(state):
#         # print(utility(state, O))
#         return utility(state)
#     value = math.inf
#     for action in actions(state, human):
#         state[action[0]][action[1]] = action[2]
#         value = min(value, max_val(state))
#         state[action[0]][action[1]] = 0
#     return value


# def minimax(state): 
#     value = min_val(state)
#     return value



# def best_move(state):
#     allowed_moves = actions(state, computer)
#     best_score = -math.inf
#     best_move = ()
#     for move in allowed_moves:
#         state[move[0]][move[1]] = computer
#         score = minimax(state)
#         state[move[0]][move[1]] = 0
#         # print(move, score)
#         if score > best_score:
#             best_score = score
#             best_move = move
#     result(state, best_move)

# board = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]


# def print_state(state):
#     for row in state:
#         for element in row:
#             # print("element:", element)
#             print(('X' if element == X else 'O' if element == O else '_'), end='\t')
#         print('')
#     print('------------------\n')

# numpad_move_lookup={
#     1:(2,0,human),
#     2:(2,1,human),
#     3:(2,2,human),
#     4:(1,0,human),
#     5:(1,1,human),
#     6:(1,2,human),
#     7:(0,0,human),
#     8:(0,1,human),
#     9:(0,2,human)
# }

# def main():
#     print_state(board)
#     while not is_terminal(board):

#         try:
#             if computer == X:
#                 best_move(board)  
#                 print_state(board)

#                 result(board, numpad_move_lookup[int(input("where to?:"))])
#                 print_state(board)
#             else:
#                 result(board, numpad_move_lookup[int(input("where to?:"))])
#                 print_state(board)  

#                 best_move(board)  
#                 print_state(board)  

 
#         except Exception as e:

#             print_state(board)
#             print(e)
#             continue

        

        
        
        

# # main()


# print()

game = TicTacToe(True)
game.play()