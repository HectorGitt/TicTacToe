from tkinter import *
import random, time
count = 0
def callback(r, c):
    global initial
    global Player
    global count
    if (Player == "X") and (initial[r][c] == 0) and (cont_game == True):
        b[r][c].configure(text="X")
        initial[r][c]= "X"
        Player = "O"
        count += 1
        verif_win()
    if (Player == "O") and  (cont_game == True):
        
        Computer()    
    
def Computer():
    global initial
    global Player
    global count
    AI = [0, 1, 2]
    bot = random.choice(AI)
    bot1 = random.choice(AI) 
    
    if (Player == "O") and (initial[bot][bot1]== 0) and  (cont_game == True):
        b[bot][bot1].configure(text="0")
        initial[bot][bot1] = "O"
        Player = "X"
        count += 1
    elif (Player == "O") and (initial[bot][bot1] != 0) and  (cont_game == True):
        Computer()
    verif_win()

initial = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

b = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]] 
def verif_win():
    global count
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
    if count == 9:
        cont_game = False
def clear():
    global b
    global initial
    global Player
    global cont_game 
    cont_game = True
    for i in range(3):
        for j in range(3):
            b[i][j] = Button(bg="pink")
            b[i][j].configure(text="")
    initial = b        
    Player = "X"
    

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=("Verdana", 50), width = 3, height = 1, bg="pink",
            command= lambda r= i,c=j: callback(r,c))
        b[i][j].grid(row = i, column = j)
Closebutton = Button(text="Restart", command= clear)
Closebutton.grid(row =3, column= 0, columnspan =2)
Player = "X"
cont_game = True
mainloop() 