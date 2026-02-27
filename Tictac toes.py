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
        return True
        

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

if board[0][0] == board[1][1] == board[2][2] == current_player:
    print(f"{current_player} wins")
    return True

if board[0][2] == board[1][1] == board[2][0] == current_player:
    print(f"{current_player} wins")
    return True

    
for row in board:
    for space in row:
        if space == 0:
            return False
        
def main():
    grid = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    curr = "A"

    while checkwinner(grid,curr) == False:
        curr = switchplayer(curr)
        check = False:
        while check == False:
            row = int(input{"enter the row"}.strip())
            3210.        

if __name__ == "__main__":
    main()