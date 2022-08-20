def PrintBoard(xIndex, zIndex):
    zero = 'X' if xIndex[0] else ('O' if zIndex[0] else 0)
    one = 'X' if xIndex[1] else ('O' if zIndex[1] else 1)
    two = 'X' if xIndex[2] else ('O' if zIndex[2] else 2)
    three = 'X' if xIndex[3] else ('O' if zIndex[3] else 3)
    four = 'X' if xIndex[4] else ('O' if zIndex[4] else 4)
    five = 'X' if xIndex[5] else ('O' if zIndex[5] else 5)
    six = 'X' if xIndex[6] else ('O' if zIndex[6] else 6)
    seven = 'X' if xIndex[7] else ('O' if zIndex[7] else 7)
    eight = 'X' if xIndex[8] else ('O' if zIndex[8] else 8)
    
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")
    print(f"--|---|--")
    
def sum(a, b, c):
    return a + b + c

def checkwin(xIndex, zIndex):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xIndex[win[0]],xIndex[win[1]], xIndex[win[2]]) == 3:
            print("X is winner")
            return 1
        if sum(zIndex[win[0]],zIndex[win[1]], zIndex[win[2]]) == 3:
            print("Z is winner")
            return 0
    return -1

xIndex = [0, 0, 0, 0 ,0, 0, 0, 0, 0]
zIndex = [0, 0, 0, 0 ,0, 0, 0, 0, 0]  
turn = 1  
print("Let's Play 'Tic Tac Toe!!")
while True:
    PrintBoard(xIndex, zIndex)
    if turn == 1:
        print("X's turn !! ")
        value = int(input("Enter a value: "))
        xIndex[value] = 1     
    else:
        print("0's turn !! ")
        value = int(input("Enter a value: "))
        zIndex[value] = 1
        checkwin(xIndex, zIndex)
    cwin = checkwin(xIndex, zIndex)
    if cwin != -1:
        print("Game Over")
        break
    turn = 1 - turn
