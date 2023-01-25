import time
import array
from tkinter import *

def drop(row, col, colour):
  if colour == 90:
    colours = 'grey1'
    button[row][col].config(bg=colours)
    list32x32[row][col] = colour
  elif colour == 0:
    colours = 'grey99'
    button[row][col].config(bg=colours)
    list32x32[row][col] = colour

def empty(board, col):
  return board[8-1][col] == 0

def get_next_open_row(col):
  for i in range(7, -1, -1): #7, 6, 5, 4, 3, 2, 1, 0
    if list32x32[i][col] == 50:
      return i

def whitebtn(j):
  global colour
  row = get_next_open_row(j)
  if row != None:
    if colour == 0:
        button[i][j].config(bg='grey44')
        list32x32[i][j] = 50   
    elif colour == 1:
        drop(row, j, 90)
        if button[0][7] and colour == 1:
            button[0][7].config(bg='grey0')
            list32x32[i][j] = 90
    elif colour == 2: 
        drop(row, j, 0)
  else:
    print("Column Filled")
    game_over == True

def change_colour(m): 
  global colour
  colour=m
  if colour == 0:
    print("Empty")
  elif colour == 2:
    print("Player 1 Turn!!")
  elif colour == 1:
    print("Player 2 turn!!")

#----------------------------------------------------------------------------Start, Reset & Send--------------------------------------------------------------------------------------#

def startgame():
  print("Game Start!!")
  for j in range (8):
    for i in range (8):
      button[i][j].config(bg='grey44')
      list32x32[i][j] = 50

  for i in range(32):
    for j in range(32):
      list32x32[i][j] = 50

def resetgame():
  print("Game Resetted!!")
  for j in range (8):
    for i in range (8):
      button[i][j].config(bg='grey44')
      list32x32[i][j] = 50
  
  for i in range(32):
    for j in range(32):
      list32x32[i][j] = 50

def sendImage():
  global list32x32
  print("Image has been printed, the values are.....")
  print(list32x32)

# value[0][0]
list32x32 = [[0 for i in range(32)] for j in range(32)]

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
frame4.grid(row=4, column=0) #Reset btn

frame5 = Frame(main)
frame5.grid(row=4, column=1) #start btn

# -----------------------------------------------------------------------------8x8 Grid--------------------------------------------------------------------------------------------- #

button = [[j for j in range(8)] for i in range(8)]
cbutton = [[j for j in range(8)] for i in range(8)]

list32x32 = [[0 for j in range(32)] for i in range (32)]

# Main Buttons
for j in range (8):
  for i in range (8):
    button[i][j] = Button(frame1, font=("Arial, 12"), width=6, height=3, bg='grey99')
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

send = Button(frame3, text="Send!", font=("Arial, 12"), bg='#FAA0A0', width=13, height=2, command=sendImage)
send.grid(row=0, column=1)

#-----------------------------------------------------------------------Start and Reset Button----------------------------------------------------------------------------------------#

reset = Button(frame4, text="Reset",font=("Arial, 12"), bg='#DE3163', width=13, height=2, command=resetgame)
reset.grid(row=0, column=1)

start = Button(frame5, text="Start!!",font=("Arial, 12"), bg='#50C878', width=13, height=2, command=startgame)
start.grid(row=0, column=3)

main.mainloop()