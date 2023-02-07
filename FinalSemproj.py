import time
import array
from tkinter import *

def drop(row, col, colour):
  if colour == 90:
    colours = 'grey1'
    button[row][col].config(bg=colours)
    value[row][col] = colour
  elif colour == 0:
    colours = 'grey99'
    button[row][col].config(bg=colours)
    value[row][col] = colour
  sendImage()

def empty(board, col):
  return board[8-1][col] == 0

def get_next_open_row(col):
  for i in range(7, -1, -1): #7, 6, 5, 4, 3, 2, 1, 0
    if value[i][col] == 50:
      return i

def whitebtn(j):
  global colour 
  row = get_next_open_row(j)
  if row != None:
    if colour == 0:
      button[i][j].config(bg='grey44')
      value[i][j] = 50   
    elif colour == 1:
      drop(row, j, 90)
    elif colour == 2: 
      drop(row, j, 0)
  else:
    print("Column Filled")

def change_colour(m): 
  global colour
  colour=m
  if colour == 0:
    print("Empty")
  elif colour == 2:
    print("Player 1 Turn!!")
  elif colour == 1:
    print("Player 2 turn!!")

#---------------------------------------------------------------------------------All Color------------------------------------------------------------------------------------------#

def allwhite():
  print("All White!")
  for j in range (8):
    for i in range (8):
      button[i][j].config(bg='grey99')
      value[i][j] = 0

def allblack():
  print("All Black!")
  for j in range (8):
    for i in range (8):
      button[i][j].config(bg='grey1')
      value[i][j] = 90

#----------------------------------------------------------------------------Start, Reset & Send--------------------------------------------------------------------------------------#
def startgame():
  print("Game Start!!")
  for j in range (8):
    for i in range (8):
      button[i][j].config(bg='grey44')
      value[i][j] = 50

def resetgame():
  print("Game Resetted!!")
  for j in range (8):
    for i in range (8):
      button[i][j].config(bg='grey44')
      value[i][j] = 50

def sendImage():
    global value
    global game_over
    number = 0
    for i in range(8):
        for j in range(8):  
          number = value[i][j]
          for r in range(i*4, (i*4)+4):
            for c in range(j*4, (j*4)+4):
              list32[r][c] = number

    print(list32)
    print("Checking....")
    checking()

# -----------------------------------------------------------------------------------Check Win-------------------------------------------------------------------------------------------------- #
def checking():
    if game_over == False:
      for i in range(8):
        for j in range(5):
          if value[i][j] == value[i][j+1] and value[i][j+1] == value[i][j+2] and value[i][j+2] == value[i][j+3] and value[i][j+3] == value[i][j] != 50:
            if value[i][j] == 0:
              print("Player 1 Wins!!")
              lastshow(1)
              main.destroy()
            elif value[i][j] == 90:
              print("Player 2 Wins!!")
              lastshow(2)
              main.destroy()

      for i in range(5):
        for j in range(8):
          if value[i][j] == value[i+1][j] and value[i+1][j] == value[i+2][j] and value[i+2][j] == value[i+3][j] and value[i+3][j] == value[i][j] != 50:
            if value[i][j] == 0:
              print("Player 1 Wins!!")
              lastshow(1)
              main.destroy()
            elif value[i][j] == 90:
              print("Player 2 Wins!!")
              lastshow(2)
              main.destroy()

      for i in range(5):
        for j in range(5):
          if value[i][j] == value[i+1][j+1] and value[i+1][j+1] == value[i+2][j+2] and value[i+2][j+2] == value[i+3][j+3] and value[i+3][j+3] == value[i][j] != 50:
            if value[i][j] == 0:
              print("Player 1 Wins!!")
              lastshow(1)
              main.destroy()
            elif value[i][j] == 90:
              print("Player 2 Wins!!")
              lastshow(2)
              main.destroy()

      for i in range(7, 3, -1):
        for j in range(0, 4):
          if value[i][j] == value[i-1][j+1] and value[i-1][j+1] == value[i-2][j+2] and value[i-2][j+2] == value[i-3][j+3] and value[i-3][j+3] == value[i][j] != 50:
            if value[i][j] == 0:
              print("Player 1 Wins!!")
              lastshow(1)
              main.destroy()
            elif value[i][j] == 90:
              print("Player 2 Wins!!")
              lastshow(2)
              main.destroy()

def lastshow(x):
  if x == 1:
    P1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 0, 90, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 90, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 90, 90, 90, 90, 90, 90, 0, 90, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0], [0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 90, 0, 0, 0], [0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 90, 0, 0, 0], [0, 0, 0, 0, 90, 0, 90, 0, 90, 0, 90, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 90, 0, 0, 0], [0, 0, 0, 0, 90, 0, 90, 0, 90, 0, 90, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 90, 0, 0, 0], [0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0], [0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 90, 90, 90, 90, 90, 0, 90, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return P1
  elif x == 2:
    P2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90, 0, 0, 0, 0, 0, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 90, 90, 90, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 90, 90, 90, 90, 90, 90, 0, 90, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 90, 0, 0, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0], [0, 0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0], [0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 90, 0, 0, 0], [0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 90, 0, 0, 0], [0, 0, 0, 0, 90, 0, 90, 0, 90, 0, 90, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 90, 0, 0, 0], [0, 0, 0, 0, 90, 0, 90, 0, 90, 0, 90, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 90, 0, 0, 0], [0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0, 90, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0], [0, 0, 0, 0, 0, 90, 0, 0, 0, 90, 0, 0, 0, 0, 90, 90, 90, 90, 90, 90, 0, 90, 0, 0, 0, 0, 0, 90, 90, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    return P2

main = Tk()
game_over = False

# -----------------------------------------------------------------------------Frames----------------------------------------------------------------------------------------------- #

colour = 0

frame0 = Frame(main) #1x8 btn
frame0.grid(row=0, columnspan=2)

frame1 = Frame(main) #8x8 btn
frame1.grid(row=2, columnspan=2)

frame3 = Frame(main)
frame3.grid(row=3, columnspan=3) #Player and Send btn

frame4 = Frame(main)
frame4.grid(row=4, column=0) #start btn

frame5 = Frame(main)
frame5.grid(row=4, column=1) 

# -----------------------------------------------------------------------------8x8 Grid--------------------------------------------------------------------------------------------- #

button = [[j for j in range(8)] for i in range(8)]
cbutton = [[j for j in range(8)] for i in range(8)]

value = [[0 for j in range(8)] for i in range (8)]
list32 = [[50 for r in range(32)] for c in range (32)]

# Main Buttons
for j in range (8):
  for i in range (8):
    button[i][j] = Button(frame1, font=("Arial, 12"), width=6, height=3, bg='grey99')
# ------------------- Command This Line ---------------- #
    button[i][j].grid(row=i, column=j)

# Top buttons
for j in range (8):
  for i in range (1):
    cbutton[i][j] = Button(frame0, font=("Arial, 10"), width=6, height=3, bg='grey44', command=lambda c=j:whitebtn(c))
    cbutton[i][j].grid(row=i, column=j)

# --------------------------------------------------------------------------Player button-------------------------------------------------------------------------------------------- #
white = Button(frame3, text="Player 1", font=("Arial, 12"), bg='grey99', width=13, height=2, command=lambda m=2:change_colour(m))
white.grid(row=0, column=0)

black = Button(frame3, text="Player 2", font=("Arial, 12"), bg='grey1', fg='white', width=13, height=2, command=lambda m=1:change_colour(m))
black.grid(row=0, column=2)

# ---------------------------------------------------------------------------Send button--------------------------------------------------------------------------------------------- #

# send = Button(frame3, text="Send!", font=("Arial, 12"), bg='#FAA0A0', width=13, height=2, command=sendImage)
# send.grid(row=0, column=1)

#-----------------------------------------------------------------------Start and Reset Button----------------------------------------------------------------------------------------#

resetbtn = Button(frame4, text="Reset",font=("Arial, 12"), bg='#DE3163', width=13, height=2, command=resetgame)
resetbtn.grid(row=0, column=1)

startgamebtn = Button(frame5, text="Start!!",font=("Arial, 12"), bg='#50C878', width=13, height=2, command=startgame)
startgamebtn.grid(row=0, column=3)

main.mainloop()