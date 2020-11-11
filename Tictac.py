from tkinter import *
def callback(r, c):
    global initial
    global Player
    if (Player == "X") and (initial[r][c] == 0) and (cont_game == True):
        b[r][c].configure(text="X")
        initial[r][c]= "X"
        Player = "O"
    if (Player == "O") and (initial[r][c]== 0) and (cont_game == True):
        b[r][c].configure(text="0")
        initial[r][c] = "O"
        Player = "X"
    verif_win()
initial = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

b = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]] 
def verif_win():
    global cont_game
    for i in range(3):    
        if initial[i][0] == initial[i][1] == initial[i][2] != 0 :
            cont_game = False
            b[i][0].configure(bg = "grey")
            b[i][1].configure(bg = "grey")
            b[i][2].configure(bg = "grey")

    for i in range(3):    
        if initial[0][i] == initial[1][i] == initial[2][i] != 0 :
            cont_game = False
            b[0][i].configure(bg = "grey")
            b[1][i].configure(bg = "grey")
            b[2][i].configure(bg = "grey")
    if initial[0][0] == initial[1][1] == initial[2][2] != 0 :
        cont_game = False
        b[0][0].configure(bg = "grey")
        b[1][1].configure(bg = "grey")
        b[2][2].configure(bg = "grey")
    if initial[0][2] == initial[1][1] == initial[2][0] != 0 :
        cont_game = False
        b[0][2].configure(bg = "grey")
        b[1][1].configure(bg = "grey")
        b[2][0].configure(bg = "grey")
    
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=("Verdana", 50), width = 3, height = 1, bg="pink",
            command= lambda r= i,c=j: callback(r,c))
        b[i][j].grid(row = i, column = j)
Player = "X"
cont_game = True
mainloop() 