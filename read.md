# The Connect 4 Documentation

This documentation is regard the board game called Connect 4 and its features. This GUI is made to control polarised motors to display the players move. There are 2 players for this game, Player 1 being white and player 2 being black. The game would automatically detect winning and each turn the images would be sent to the display panel.

# Completed GUI
![GUI](/EGL314%Repo%resouces/Final Gui.PNG) <br>
*Photo of Completed GUI*

# Hardware Used
**Model of hardware** : RaspberryPi 4 Model B <br>
**Version** : Raspbian GNU Linux 10 Buster <br><br>
![RaspberryPi](/resources/rasp.PNG) <br>
*Photo of Raspberry Pi*
---
---
[Source](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

# Frame Function
**Frame 0** is for the 1x8 grid.
```
frame0 = Frame(main) #1x8 btn
frame0.grid(row=0, columnspan=2)
```
**Frame 1** is for the 8x8 buttons. 
```
frame1 = Frame(main) #8x8 btn
frame1.grid(row=2, columnspan=2)
```
**Frame 3** is for the Player and send buttons. 
```
frame3 = Frame(main)
frame3.grid(row=3, columnspan=3) #Player and Send btn
```
**Frame4** is for the Reset button. 
```
frame 4 = Frame(main)
frame4.grid(row=4, column=0) #Reset btn
```
**Frame 5** is for the Start button. 
```
frame5 = Frame(main)
frame5.grid(row=4, column=1) #start btn
```

# Create 8x8 Buttons
The 8x8 buttons are made by **nested for loop** that is inside the list 'button'
```
#Main Buttons
for j in range (8):
  for i in range (8):
    button[i][j] = Button(frame1, font=("Arial, 12"), width=6, height=3, bg='grey99')
    button[i][j].grid(row=i, column=j)
```

![GUI](/resources/8x8btn.PNG) <br>
*Photo of 8 x 8 Grid*

<br>

# Create player Buttons
These buttons will change to the player's color when the following player is selected.
```
white = Button(frame3, text="Player 1", font=("Arial, 12"), bg='grey99', width=13, height=2, command=lambda m=2:change_colour(m))
white.grid(row=0, column=0)

black = Button(frame3, text="Player 2", font=("Arial, 12"), bg='grey1', fg='white', width=13, height=2, command=lambda m=1:change_colour(m))
black.grid(row=0, column=2)
```

## Creating a variable to store colour value. 
```
colour = 0
```
**Lambda** will be used for the shade button for the 8 x 8 GUI. **Lambda** is used when we require a nameless function for a short period of time. 
```
def change_colour(m): 
  global colour
  colour=m
  if colour == 0:
    print("Empty")
  elif colour == 2:
    print("Player 1 Turn!!")
  elif colour == 1:
    print("Player 2 turn!!")
```

Using if else statement to create function for the change of colors. 
```
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
```

# All Buttons 
These are all the buttons that are used for the GUI for player to press and play on.
```
white = Button(frame3, text="Player 1", font=("Arial, 12"), bg='grey99', width=13, height=2, command=lambda m=2:change_colour(m))
white.grid(row=0, column=0)

black = Button(frame3, text="Player 2", font=("Arial, 12"), bg='grey1', fg='white', width=13, height=2, command=lambda m=1:change_colour(m))
black.grid(row=0, column=2)

reset = Button(frame4, text="Reset",font=("Arial, 12"), bg='#DE3163', width=13, height=2, command=resetgame)
reset.grid(row=0, column=1)

start = Button(frame5, text="Start!!",font=("Arial, 12"), bg='#50C878', width=13, height=2, command=startgame)
start.grid(row=0, column=3)
```

![GUI](/EGL314 Repo resouces/All btn.PNG) <br>
*Photo of all buttons*

Code for Start btn
```
def startgame():
  print("Game Start!!")
  for j in range (8):
    for i in range (8):
      button[i][j].config(bg='grey44')
      value[i][j] = 50
```

Code for Reset btn
```
def resetgame():
  print("Game Resetted!!")
  for j in range (8):
    for i in range (8):
      button[i][j].config(bg='grey44')
      value[i][j] = 50
```

Code for Send and Check win
```
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
```

Code to check for empty row <br>
This code checks the column for an empty space, if found the players would then be able to place their piece on the space.
```
def empty(board, col):
  return board[8-1][col] == 0
```

Code to check for player's game piece <br>
This will prevent the changing of player's colour and will only affect the default game board. Automatically sends the image to the Panel.
```
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
```

Code to check for max column <br>
This will prevent players from adding on or overwriting the pieces during the game.
```
def get_next_open_row(col):
  for i in range(7, -1, -1): #7, 6, 5, 4, 3, 2, 1, 0
    if value[i][col] == 50:
      return i
```
