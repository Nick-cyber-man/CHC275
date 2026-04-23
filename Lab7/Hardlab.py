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
        
def switchPlayer(current_player):
    if current_player == "B":
        return "W"
    elif current_player == "W":
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
    
    #recursive Case 
    
    #part 1: find the current player
    for x in range(len(board)):
        for y in range(len(board[0])):
            try:
                if board[x][y] == board[x+1][y] == board [x+2][y] == board[x+3][y] == player:
                    return True
    #part 2a
    if board[x][y] == board[x][y+1] == board [x + 1][y] == player and board[x+1][y+1] == '.':
        floodfill(board,x+1,y+1,player)
        return True
    
    
   #part 2b
   
   
   #part 3: recursively call find_inside until you get to the bottom right
        
        

def main():
    board = loadBoard("board.txt")
    printBoard(board)
    find_inside(board,0,0,"B")
    print()
    printBoard(board)
if __name__ == "__main__":
    main()