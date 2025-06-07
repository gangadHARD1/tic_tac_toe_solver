"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
count=1





def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player():
    global count
    if count %2==0:
        count+=1
        return "X"
    else:
        count+=1
        return "O"
    
    '''x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)
    return "X" if x_count == o_count else "O"'''
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    poss=[]
    for i in range( len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                poss.append((i,j))
    #player(board)
    return poss
    raise NotImplementedError


def result(board, action,player):
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #print(board ,"&&&&&&&&&&")
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    """
    if winner(board) == "X":         
        return 1
    elif winner(board) == "O":
        return -1
    elif winner(board) is None:
        return 0
   


def minimax(board,player):
    """
    Returns the optimal action for the current player on the board.
    """
    def minmove(board,prune_val):
         if terminal(board)==True:
             return utility(board)
         v=2
         for poss in actions(board):
              newb=copy.deepcopy(board)
              newb[poss[0]][poss[1]]="O"
              v=min(v,maxmove(newb,v))
              if v<prune_val:
                  break
            
         return (v)
    def maxmove(board,prune_val):
         if terminal(board)==True:
             return utility(board)
         v=-2
         for poss in actions(board):
              newb=copy.deepcopy(board)
              newb[poss[0]][poss[1]]="X"
              v=max(v,minmove(newb,v))
              if v>prune_val:
                  break
         return (v) 
    ans=None           
    if player=="X":
        v=-2
        for poss in actions(board):
            newb=copy.deepcopy(board)
            newb[poss[0]][poss[1]]="X"
            nxt=minmove(newb,v)
            if nxt>v:
                ans=(poss[0],poss[1])
                v=nxt
                if v==1:
                    break
                
            
    else:
        v=+2
        for poss in actions(board):
            newb=copy.deepcopy(board)
            newb[poss[0]][poss[1]]="O"
            nxt=maxmove(newb,v)
            if nxt<v:
                ans=(poss[0],poss[1])
                v=nxt
                if v==-1:
                    break
                
    return ans