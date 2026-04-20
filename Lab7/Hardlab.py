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
    pass




    
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

def find_inside(board):
       pass


def main():
    board = loadBoard("board.txt")
    printBoard(board)
if __name__ == "__main__":
    main()