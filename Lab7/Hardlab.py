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
    if x == len(board)-1 and y == len(board[0])-1:
        return True
    try:
        if board[x][y] == "B":
            player = "B"
        if board[x][y] == "W":
            player = "W"
        
        if board[x][y] == board[x][y+1] == board [x + 1][y] == player and board[x+1][y+1] == '.':
            floodfill(board,x+1,y+1,player)
            return True
    
        if board[x][y] == board [x][y + 1] == board[x+1][y-1] == player and board[x+1][y] == '.':
            floodfill(board,x+1,y,player)
            return True
   
    finally:
        if y < len(board[0])-2:    
            find_inside(board,x,y+1,player)
        if x < len(board)-2:
            find_inside(board,x+1,y,player)
        
def main():
    boardfinal = loadBoard("board.txt")
    printBoard(boardfinal)
    find_inside(boardfinal,0,0,"B")
    print()
    printBoard(boardfinal)
    scores = countScore(boardfinal)
    if scores[0] > scores[1]:
        print("Black is the winner")
    if scores[0] < scores[1]:
        print ("White is the winner")
    if scores[0] == scores[1]:
        print("The game is a tie")
if __name__ == "__main__":
    main()