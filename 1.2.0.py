import random
board=[[" "," "," "],[" "," "," "],[" "," "," "]]
coords=[["3 1","3 2","3 3"],["2 1","2 2","2 3"],["1 1","1 2","1 3"]]
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
def place(board, place, ai):
    if ai == False :
        print(place, "turn")
        ycoord=int(input("y coord: "))-1
        xcoord=int(input("x coord: "))-1
        if board[ycoord][xcoord] == " ":
            board[ycoord][xcoord]=place
        else :
            input("Why are you trying to cheat? ")
    else:
        ycoord=random.randint(1,3)
        xcoord=random.randint(1,3)
        while board[ycoord][xcoord] != " ":
            ycoord=random.randint(1,3)
            xcoord=random.randint(1,3)
        board[ycoord][xcoord]=place
        
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
if playernum == "1" :
    while True:
        place(board, "X", False)
        if checkwin(board, "X") == True :
             print("X wins!")
             showb(board)
             break
        place(board, "O", True)
        if checkwin(board, "O") == True :
            print("O wins!")
            showb(board)
            break
        showb(board)
elif playernum== "2" :
    while True:
        place(board, "X", False)
        showb(board)
        if checkwin(board, "X") == True :
             print("X wins!")
             break
        place(board, "O", False)
        showb(board)
        if checkwin(board, "O") == True :
            print("O wins!")
            break
  
input()
