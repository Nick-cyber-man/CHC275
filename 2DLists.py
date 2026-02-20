grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],    
]

print(grid[0][0])


grid2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(grid2[2][2])

for row in grid2:
    for num in row:
        print(num)
        

for i in range(len(grid2)):
    for j in range(len(grid2[0])):
        print(f"grid2{i},{j}) = {grid2[i][j]}", end = " ")
    print()
    
    
    
    
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

current_player = "0"

def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|", end = "|")
            print(board[i][j],end = "|")
            print()
            
printboard(board)
print("--------")


def placedpiece(board,current_player,row,col):
    if board[row][col] == 0:
        board[row][col] = current_player
    else:
        print("that is not a walid square")

def switchplayer(current_player):
    if current_player == "O":
        return "x"
    elif current_player == "x":
        return "O"

def checkwinner(baord, current_player):
    for i in range(len(board)):
        if board[i][0] == current_player and board[i][1] == current_player and board[i][2] == current_player:
            print(f"{current_player} wins!")
            return True
    for j in range(len(board[0])):
        if board[0][j] == current_player and board[1][j] == current_player and board[2][j] == current_player:
            print(f"{current_player} wins!")
            return True
print()
placedpiece(board)
printboard(board)

    


    