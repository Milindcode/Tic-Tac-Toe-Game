import tkinter
from tkinter import *   

window= Tk()
window.title("Tic Tac Toe")
window.geometry("1000x1000")

frame= Frame(window, bg='green')
frame.place(relheight=1/2, relwidth=1/2, relx=1/4, rely=1/4)

label = Label(text= "X's turn", font=('consolas',40))
label.pack(side="top")

button=[['.','.','.'],['.','.','.'],['.','.','.']]
arr=[['.','.','.'],['.','.','.'],['.','.','.']]
def checkspaces():
    count=0
    for i in range(0,3):
        for j in range(0,3):
            if arr[i][j]=='.':
                count+=1
    return count

def wincheck():

    for i in range(0,3):
        if button[0][i]==button[1][i] == button[2][i]!= '.':
            return True

    for i in range(0,3):
        if button[i][0]==button[i][1] == button[i][2]!= '.':
            return True

    if button[0][0]==button[1][1]==button[2][2] != '.':
            return True

    elif button[0][2]==button[1][1]==button[2][0]!= '.':
            return True

    elif checkspaces()!=0:
        return False
    else:
        return "tie"


players=['X', 'O']
player=players[0]


g,draw=0,0
def turn(row, column):
    global g, draw
    if wincheck()==False:

        if checkspaces()==0:
            label.config(text="DRAW")
            draw+=1

        elif g%2==0:
            if arr[row][column]=='.':
                button[row][column].config(text='X')
                arr[row][column]= 'X'
                button[row][column]= 'X'
                label.config(text="O's Turn")
                g+=1
            else:
                label.config(text="Invalid Input")    
        elif g%2!=0:
            if arr[row][column]=='.':
                button[row][column].config(text='O')
                arr[row][column]= 'O'
                button[row][column]= 'O'
                label.config(text="X's Turn")
                g+=1
            else:
                label.config(text="Invalid Input")   

    if wincheck() is True:
        if g%2==0:
            label.config(text="O wins")
        else:
            label.config(text="X wins")

for row in range(3):
    for column in range(3):
        button[row][column] = Button(frame, text=arr[row][column] ,font=('consolas',40),
                                      command= lambda x=row, y=column: turn(x,y))
        button[row][column].place(relx=column/3, rely=row/3, relheight=1/3, relwidth=1/3)

print(wincheck())



#button[i][j].place(relx=j/3, rely=i/3, relheight=1/3, relwidth=1/3)

# button[0][0].configure(command=lambda i=0, j=0: turn(i,j))
# button[0][1].configure(command=lambda i=0, j=1: turn(i,j))
# button[0][2].configure(command=lambda i=0, j=2: turn(i,j))
# button[1][0].configure(command=lambda i=1, j=0: turn(i,j))
# button[1][1].configure(command=lambda i=1, j=1: turn(i,j))
# button[1][2].configure(command=lambda i=1, j=2: turn(i,j))
# button[2][0].configure(command=lambda i=2, j=0: turn(i,j))
# button[2][1].configure(command=lambda i=2, j=1: turn(i,j))
# button[2][2].configure(command=lambda i=2, j=2: turn(i,j))

window.mainloop()   