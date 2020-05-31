from tkinter import *
from random import *
from tkinter import messagebox
start =Tk()
start.configure(background="purple")
start.title("welcome")
start.geometry("400x400")
count=1
def click():
    if bt1["text"]==bt2["text"] and bt1["text"]==bt3["text"]:
        if bt1["text"]=="X":
            messagebox.showinfo("win","--player1 won--")
        elif bt1["text"]=="O":
            messagebox.showinfo("win","--player2 won--")
    elif bt1["text"]==bt4["text"] and bt1["text"]==bt7["text"]:
        if bt1["text"]=="X":
            messagebox.showinfo("win","--player1 won--")
        elif bt1["text"]=="O":
            messagebox.showinfo("win","--player2 won--")
    elif bt3["text"]==bt6["text"] and bt3["text"]==bt9["text"]:
        if bt3["text"]=="X":
            messagebox.showinfo("win","player1 won--")
        elif bt3["text"]=="O":
            messagebox.showinfo("win","--player2 won--")
    elif bt1["text"]==bt5["text"] and bt1["text"]==bt9["text"]:
        if bt1["text"]=="X":
            messagebox.showinfo("win","--player1 won--")
        elif bt1["text"]=="O":
            messagebox.showinfo("win","--player2 won--")
    elif bt3["text"]==bt5["text"] and bt3["text"]==bt7["text"]:
        if bt3["text"]=="X":
            messagebox.showinfo("win","--player1 won--")
        elif bt3["text"]=="O":
            messagebox.showinfo("win","--player2 won--")
    elif bt7["text"]==bt8["text"] and bt7["text"]==bt9["text"]:
        if bt7["text"]=="X":
            messagebox.showinfo("win","--player1 won--")
        elif bt7["text"]=="O":
            messagebox.showinfo("win","--player2 won--")
    elif bt4["text"]==bt5["text"] and bt5["text"]==bt6["text"]:
        if bt4["text"]=="X":
            messagebox.showinfo("win","--player1 won")
        elif bt4["text"]=="O":
            messagebox.showinfo("win","--player2 won--")
    elif bt2["text"]==bt5["text"] and bt2["text"]==bt8["text"]:
        if bt2["text"]=="X":
            messagebox.showinfo("win","--player1 won")
        elif bt2["text"]=="O":
            messagebox.showinfo("win","--player2 won--")
def fun(a):
    global count
    if a==1 and bt1["text"]==" ":
        if count%2==0:
            bt1["text"]="O"
        else:
            bt1["text"]="X"
        count+=1
        click()
    elif a==2 and bt2["text"]==" ":
        if count%2==0:
            bt2["text"]="O"
        else:
            bt2["text"]="X"
        count+=1
        click()
    elif a==3 and bt3["text"]==" ":
        if count%2==0:
            bt3["text"]="O"
        else:
            bt3["text"]="X"
        count+=1
        click()
    elif a==4 and bt4["text"]==" ":
        if count%2==0:
            bt4["text"]="O"
        else:
            bt4["text"]="X"
        count+=1
        click()
    elif a==5 and bt5["text"]==" ":
        if count%2==0:
            bt5["text"]="O"
        else:
            bt5["text"]="X"
        count+=1
        click()
    elif a==6 and bt6["text"]==" ":
        if count%2==0:
            bt6["text"]="O"
        else:
            bt6["text"]="X"
        count+=1
        click()
    elif a==7 and bt7["text"]==" ":
        if count%2==0:
            bt7["text"]="O"
        else:
            bt7["text"]="X"
        count+=1
        click()
    elif a==8 and bt8["text"]==" ":
        if count%2==0:
            bt8["text"]="O"
        else:
            bt8["text"]="X"
        count+=1
        click()
    elif a==9 and bt9["text"]==" ":
        if count%2==0:
            bt9["text"]="O"
        else:
            bt9["text"]="X"
        count+=1
        click()
bt1 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(1))
bt1.place(x=120,y=100)
bt2 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(2))
bt2.place(x=171,y=100)
bt3 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(3))
bt3.place(x=222,y=100)
bt4 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(4))
bt4.place(x=120,y=155)
bt5 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(5))
bt5.place(x=171,y=155)
bt6 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(6))
bt6.place(x=222,y=155)
bt7 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(7))
bt7.place(x=120,y=210)
bt8 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(8))
bt8.place(x=171,y=210)
bt9 = Button(start, text=" ", height=3, width=6, bg="bisque", command=lambda:fun(9))
bt9.place(x=222,y=210)
start.mainloop()