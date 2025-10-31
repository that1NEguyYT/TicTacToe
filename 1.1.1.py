board=[[" "," "," "],[" "," "," "],[" "," "," "]]
#startup screen
print("""░▀▀█▀▀░▀█▀░▒█▀▀▄░░░░▀▀█▀▀░█▀▀▄░▒█▀▀▄░░░░▀▀█▀▀░▒█▀▀▀█░▒█▀▀▀
░░▒█░░░▒█░░▒█░░░░▀▀░░▒█░░▒█▄▄█░▒█░░░░▀▀░░▒█░░░▒█░░▒█░▒█▀▀▀
░░▒█░░░▄█▄░▒█▄▄▀░░░░░▒█░░▒█░▒█░▒█▄▄▀░░░░░▒█░░░▒█▄▄▄█░▒█▄▄▄
""")
print("Welcome!")
print("""- 1 - Singleplayer
- 2 - Multiplayer""")
playernum=input(">>")
#shows board
def showb(board):
    print(board[2])
    print(board[1])
    print(board[0])
#places item on board
def place(board, place):
    print(place, "turn")
    ycoord=int(input("y coord: "))-1
    xcoord=int(input("x coord: "))-1
    if board[ycoord][xcoord] == " ":
        board[ycoord][xcoord]=place
    else :
        input("Why are you trying to cheat? ")
#checks if there is a winner
def checkwin(board, place) :
    if board[2][0] == place and board[2][1] == place and board[2][2] == place :
        return True
    elif board[1][0] == place and board[1][1] == place and board[1][2] == place :
        return True
    elif board[0][0] == place and board[0][1] == place and board[0][2] == place :
        return True
    elif board[0][0] == place and board[1][0] == place and board[2][0] == place :
        return True
    elif board[0][1] == place and board[1][1] == place and board[2][1] == place :
        return True
    elif board[0][2] == place and board[1][2] == place and board[2][2] == place :
        return True
    elif board[2][0] == place and board[1][1] == place and board[0][2] == place :
        return True
    elif board[2][2] == place and board[1][1] == place and board[0][0] == place :
        return True
#main run
if playernum== "2" :
    while True:
        place(board, "X")
        showb(board)
        if checkwin(board, "X") == True :
             print("X wins!")
             break
        place(board, "O")
        showb(board)
        if checkwin(board, "O") == True :
            print("O wins!")
            break
input()
