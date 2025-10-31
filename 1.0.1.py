board=[[" "," "," "],[" "," "," "],[" "," "," "]]
def showb(board):
    print(board[2])
    print(board[1])
    print(board[0])
def place(board, place):
    print(place, "turn")
    ycoord=int(input("y coord"))-1
    xcoord=int(input("x coord"))-1
    if board[ycoord][xcoord] == " ":
        board[ycoord][xcoord]=place
    else :
        print("Why are you trying to cheat? ")
while True:
    showb(board)
    place(board, "X")
    showb(board)
    place(board, "O")
