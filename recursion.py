def CountDown(n):
    print(n)
    CountDown(n-1)
CountDown(5)

def factorial(x):
    if x ==1:
        return 1
    return x * factorial(x-1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)
    for n in range(10):
        print(fib(n))
        
        
def recursivePalindrome(word):
    if len(len) == 1 or len(word) == 0:
        return True
    if word(0) == word(-1):
        return recursivePalindrome(word[1:-1])
    return False

def validmove(board,x,y):
    return board[x][y] == 0 and 0 <= x < len(board) and 0 <= y <len(board[0])

def buildpath(board,x,y,path):
    if x == len(board) - 1 and y == len(board[0]) - 1:
        path.append((x,y))
        return path
    
    if validmove(board,x,y):
        path.append((x,y))
        
        if builpath(board,x,y+1,path):
            return True

        if buildpath(board,x+1,y,path):
            return true

        path.pop
    return False

def search(board):
    path = []
    buildpath(board,0,0,path)
    return path

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
    
if __name__ == "__main__":
    main()
    
print(search(board))

num1 = [num*2 for num in range(999)]

def linearsearch(num,target):
    for i in range(len(num)):
        if num[i] == target:
            return 1
    
    return False