def drawBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|", end = "")
            print(board[i][j],end = "|")
        print()

    print("--------")
    
    
current_player = "X"

def switchPlayer(player):
    if current_player == "O":
        return "x"
    elif current_player == "x":
        return "O"

    
def dropPiece(board,current_player,col,):
    if board[][col] == 0:
        board[r][col] = current_player
    else:
        print("that is not a valid square")
        return True
    

    """ 
    Drops piece in specified column
    
        PARAMETERS:
        board (2D List): Game board
        player (STR): current player
        column (int): column to drop piece in
        
        Return Type:
        NONE
    """

    
    
def checkWinner(board,player):
    """
    Checks Board for winner
    
        PARAMETERS:
        board(2d list): Game board
        player(STR): Current player being checked for victory   
        
        Return Type:
        (BOOL): True if win False if not win 
    """
    #Check Horizontal Win

    
    #Check Vertical Win


    #Check Left Diagonal win
 
    
    #Check Right Diagonal Win

    

def main():
    ROWS = 6
    COLUMNS = 7
    BOARD = [ 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],        
    ]
    current_player = "x"
    #current_player = switchPlayer()
    drawBoard(BOARD)

    
if __name__ == "__main__":
    main()
    
    
# j = chosen by the player (1)
#i = 0


#0 0 i,j
#0 0 i+1,j
#0 x i+2,j = curr
0 x
0 x

i,j i = 2 j =1

board[i-1][j] = curr

if board[i][j] != 0:
   board[i-1][j] = curr
   return True
else:
   i = i + 1


0 0 
0 0
0 0 
0 0


1) just check the top piece if its full
2) while loop
3) fill the last spot, (board[5][j] = curr)