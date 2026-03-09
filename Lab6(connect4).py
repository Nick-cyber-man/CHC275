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
        for j in range(len(board[0])):
            try:
                if board[i][j] == board[i+1][j] == board [i+2][j] == board[i+3][j] == current_player:
                    print(f"{current_player} has got four in a row")
                    return True
            except Exception as e:
                pass
    for i in range(len(board)):
        for j in range(len(board[0])):
            try:
                if board[i][j] == board[i][j+1] == board [i][j+2] == board[i][j+3] == current_player:
                    print(f"{current_player} has got four in a row")
                    return True
            except Exception as e:
                pass
    for i in range(len(board)):
        for j in range(len(board[0])):
            try:
                if board[i][j] == board[i+1][j+1] == board [i+2][j+2] == board[i+3][j+3] == current_player:
                    print(f"{current_player} has got four in a row")
                    return True
            except Exception as e:
                pass
    for i in range(len(board)):
        for j in range(len(board[0])):
            try:
                if board[i][j] == board[i+1][j-1] == board [i+2][j-2] == board[i+3][j-3] == current_player:
                    print(f"{current_player} has got four in a row")
                    return True
            except Exception as e:
                pass    
    for row in board:
        for space in row:
            if space == 0:
                return False
    return True
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
    curr = "x"
    while checkWinner(BOARD,curr) == False:
        drawBoard(BOARD)
        curr = switchPlayer(curr)
        check = False
        while check == False:
            col = int(input(f"{curr} enter the Column").strip())
            if dropPiece(BOARD,curr,col):
                check = True
            
if __name__ == "__main__":
    main()
