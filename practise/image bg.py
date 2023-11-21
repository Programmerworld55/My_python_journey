from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry("800x700")
c=Canvas(win,bg="gray",height=200,width=200)
filename=PhotoImage('C:/Users/JK.tech/Desktop/os image/pics2/pics3/1.png')
background_label=Label(win,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
c.pack()
win.mainloop()



