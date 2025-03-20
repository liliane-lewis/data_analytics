#!/usr/bin/python3



pieces = [[" " for _ in range(3)] for _ in range(3)]
coordenates = [["0,0","0,1","0,2"],["1,0","1,1","1,2"],["2,0","2,1","2,2"]]


def display_board(board):
    print(" " * 10 + "*******************************")  
    for i in range(3):
        print(" " * 10 + f"*  {board[i][0].center(5)}  |  {board[i][1].center(5)}  |  {board[i][2].center(5)}  *")
        if i < 2:
            print(" " * 10 + "*   ----- |  -----  |  -----  *")
    print(" " * 10 + "*******************************")



def player_input(player):

    while True:
        display_board(pieces)
        print(f"Player {player}'s turn...")
        coord = input("Write the coordenate. eg: 0,0. Type 'c' to see the coordenates:\n")

        if coord.lower() == 'c':
            display_board(coordenates)
            continue
        
        try:
            x, y = map(int, coord.split(","))
            if pieces[x][y] not in ["X", "O"]: 
                pieces[x][y] = player
                break
            else:
                print("This position has already been chosen! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Enter a valid coordinate, such as '0,0'.")


    
def check_win():
    for i in range(3):
        if pieces[i][0] == pieces[i][1] == pieces[i][2] and pieces[i][0] != " ":
            return True  # Row
        if pieces[0][i] == pieces[1][i] == pieces[2][i] and pieces[0][i] != " ":
            return True  # Column
        
    if pieces[0][0] == pieces[1][1] == pieces[2][2] != " ":
        return True   #diagonals
    if pieces[0][2] == pieces[1][1] == pieces[2][0] != " ":
        return True   #diagonals   

def check_draw():
    for row in pieces:
        for cell in row:
            if cell not in ["X", "O"]:
                return False
    return True

def play():

    print("Welcome to TIC TAC TOE!")
    display_board(coordenates)

    player = "X"  # first player
    while True:
        player_input(player)
        if check_win():
            display_board(pieces)
            print(f"Congratulations! The player {player} won!")
            break
        if check_draw():
            display_board(pieces)
            print("Draw! The board is full.")
            break
        player = "O" if player == "X" else "X" 


play()