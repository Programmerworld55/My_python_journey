import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import PIL
from PIL import Image,ImageTk
import threading
import math


def create_window(t_win,w,h,title,color):
    sw = int(t_win.winfo_screenwidth() / 2)
    sh= int(t_win.winfo_screenheight()/2)
    t_win.maxsize(w,h)
    t_win.minsize(w,h)
    t_win.geometry=(f"1000x600+{sw-int(w/2)}+{sh-int(h/2)}")
    t_win.title(title)
    t_win.config(bg=color)
def location(event):
    print("x=",event.x,"y=",event.y)

# def shake_button():
#     x = random.randint(100, 300)
#     y = random.randint(200, 300)
#     no_B.place(x=x, y=y, anchor="center")
#     win.after(300, shake_button)
def shake_button():
    x = random.randint(100, 300)
    y = random.randint(200, 300)
    dist_x = x - no_B.winfo_pointerx()
    dist_y = y - no_B.winfo_pointery()
    dist = math.sqrt(dist_x**2 + dist_y**2)
    if dist < 100:
        no_B.place(x=x, y=y, anchor="center")
    win.after(50, shake_button)



def yes(win):
    win.destroy()
    win=Tk()
    create_window(win, 400, 300, "Script Kiddies", "grey")
    create_img(win, "10.webp", 400, 300)
    q2_label = tk.Label(win, text="i knew IT----------------<3", bg="grey", fg="black", font=("", 20, "bold"))
    q2_label.place(x=63, y=122)
def create_img(contanior,img,w,h):
    img=Image.open(img).resize((w,h))
    imgtk=ImageTk.PhotoImage(img)
    lab=tk.Label(contanior)
    lab.config(image=imgtk,bd=0)
    lab.image=imgtk
    lab.place(x=0,y=0)
    return lab
win=Tk()
create_window(win,400,300,"Script Kiddies","grey")
create_img(win,"10.webp", 400, 300)
q_label=tk.Label(win,text="Are U Dumb........??",bg="grey",fg="black",font=("",20,"bold"))
q_label.place(x= 63,y= 122)
yes_B=Button(win,text="Yes",bg="black",fg="white",width=3,height=1,font=("",12,"bold"),command=lambda:yes(win))
yes_B.place(x= 125,y= 180)
no_B=tk.Button(win,text="No",bg="black",fg="white",width=3,height=1,state="disable",font=("",12,"bold"))
no_B.place(x= 220,y= 180)
win.bind("<Button-1>", lambda event: location(event))
win.after(100, shake_button)
win.mainloop()

