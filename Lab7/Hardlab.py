def loadBoard(filename):
    board = []
    file = open("board.txt", "r")
    buffer = file.readlines()
    for line in buffer:
        line = line.strip()
        line = list(line)
        board.append(line)
    return board
    
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end = "")
        print()
        
def switchPlayer(player):
    if player == "B":
        return "W"
    elif player == "W":
        return "B"





    
def floodfill(matrix, x, y, color):
    if matrix[x][y] == ".":  
        matrix[x][y] = color 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill(matrix,x-1,y,color)
        if x < len(matrix[x]) - 1:
            floodfill(matrix,x+1,y,color)
        if y > 0:
            floodfill(matrix,x,y-1,color)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1,color)


def countScore(board):
    pass

def find_inside(board,x,y,player):
    #Base Case: bottom right
    print(x,y)
    if x == len(board)-1 and y == len(board[0])-1:
        return True
    try:
        #part 1: find the current player
        if board[x][y] == "B":
            player = switchPlayer(player)
        if board[x][y] == "W":
            player = switchPlayer(player)
    #part 2a
    
        if board[x][y] == board[x][y+1] == board [x + 1][y] == player and board[x+1][y+1] == '.':
            floodfill(board,x+1,y+1,player)
            return True
    
    
   #part 2b
        if board[x][y] == board [x][y + 1] == board[x+1][y-1] == player and board[x+1][y] == '.':
            floodfill(board,x+1,y+1,player)
            return True
   
   #part 3: recursively call find_inside until you get to the bottom right
    finally:
        if y < len(board[0])-1:    
            find_inside(board,x,y+1,player)
        if x < len(board)-1:
            find_inside(board,x+1,y,player)
        

def main():
    board = loadBoard("board.txt")
    printBoard(board)
    find_inside(board,0,0,"B")
    print()
    printBoard(board)
if __name__ == "__main__":
    main()