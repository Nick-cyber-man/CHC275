def drawBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|", end = "")
            print(board[i][j],end = "|")
        print()

    print("--------")
    

def switchPlayer(player):
    if player == "O":
        return "x"
    elif player == "x":
        return "O"

    
def dropPiece(board,current_player,col,):
    i = 0
    
    if board[0][col] == 0:
        while i < len(board):
            if board[i][col] == 0:
                i = i + 1
            else: 
                board[i-1][col] = current_player
                return True
            

    else:
        print("that is not a valid square")
        return False
    
    board[i-1][col] = current_player
    return True
    
def checkWinner(board,current_player):
    for i in range(len(board)):
            if board[i][0] == current_player and board[i][1] == current_player and board[i][2] == current_player and board[i][3] == current_player:
                print(f"{current_player} wins!")
                return True
            for col in range(len(board[0])):
                if board[0][col] == current_player and board[1][col] == current_player and board[2][col] == current_player and board[3][col] == current_player:
                    print(f"{current_player} wins!")
                    return True
            print()
            dropPiece(board)
            drawBoard(board)

    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == current_player:
        print(f"{current_player} wins")
        return True

    if board[0][3] == board[1][2] == board[2][1] == board[3][0] == current_player:
        print(f"{current_player} wins")
        return True

        
    for row in board:
        for space in row:
            if space == 0:
                return False
        

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
        #while checkwinner(grid,curr) == False:
        #curr = switchplayer(curr)
        #check = False:
        #while check == False:
            #row = int(input{"enter the row"}.strip())
            #3210.     
    drawBoard(BOARD)
    
if __name__ == "__main__":
    main()
