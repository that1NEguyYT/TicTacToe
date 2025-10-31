board=[[" "," "," "],[" "," "," "],[" "," "," "]]
#shows board
def showb(board):
    print(board[2])
    print(board[1])
    print(board[0])
#places item on board
def place(board, place):
    print(place, "turn")
    ycoord=int(input("y coord"))-1
    xcoord=int(input("x coord"))-1
    if board[ycoord][xcoord] == " ":
        board[ycoord][xcoord]=place
    else :
        print("Why are you trying to cheat? ")
#checks if there is a winner
def checkwin(board, place) :
    if board[2][0] and board[2][1] and board[2][2] == place :
        return True
    elif board[1][0] and board[1][1] and board[1][2] == place :
        return True
    elif board[0][0] and board[0][1] and board[0][2] == place :
        return True
    elif board[0][0] and board[1][0] and board[2][0] == place :
        return True
    elif board[0][1] and board[1][1] and board[2][1] == place :
        return True
    elif board[0][2] and board[1][2] and board[2][2] == place :
        return True
    elif board[2][0] and board[1][1] and board[0][2] == place :
        return True
    elif board[2][2] and board[1][1] and board[0][0] == place :
        return True
#main run
while True:
    showb(board)
    place(board, "X")
     if checkwin(board, "X") == True :
         print("X wins!")
         break
    showb(board)
    place(board, "O")
    if checkwin(board, "O") == True :
         print("O wins!")
         break
