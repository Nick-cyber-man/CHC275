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
    countblack = 0
    countwhite = 0
    for i in range(len(board)):
        for j in range(len(board[0])): 
            if board[i][j] == "B":
                countblack = countblack + 1
            if board[i][j] == "W":
                countwhite = countwhite + 1
    return [countblack,countwhite]
def find_inside(board,x,y,player):
    #Base Case: bottom right
    if x == len(board)-2 and y == len(board[0])-2:
        return True
    try:
        #part 1: find the current player
        if board[x][y] == "B":
            player = switchPlayer(player)
        if board[x][y] == "W":
            player = switchPlayer(player)
    #part 2a
    
        if board[x][y] == board[x][y+1] == board [x + 1][y] == player and board[x+1][y+1] == '.':
            print("called 1")
            floodfill(board,x+1,y+1,player)
            return True
    
    
   #part 2b
        if board[x][y] == board [x][y + 1] == board[x+1][y-1] == player and board[x+1][y] == '.':
            print("Called 2")
            floodfill(board,x+1,y+1,player)
            return True
   
   #part 3: recursively call find_inside until you get to the bottom right
    finally:
        if y < len(board[0])-2:    
            find_inside(board,x,y+1,player)
        if x < len(board)-2:
            find_inside(board,x+1,y,player)
        

def main():
    board = loadBoard("board.txt")
    printBoard(board)
    find_inside(board,0,0,"B")
    print()
    printBoard(board)
    scores = countScore(board)
    if scores[0] > scores[1]:
        print("Black is the best winner")
    if scores[0] < scores[1]:
        print ("White is the biggest winner")
    if scores[0] == scores[1]:
        print("you both drawed")
if __name__ == "__main__":
    main()