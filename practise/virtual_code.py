import os
import tkinter
from tkinter import *
import PIL
from PIL import Image,ImageTk
from tkinter import filedialog,messagebox
import threading

images=[]
extensions=['.png','.jpg','.jpeg']
total_im= 0
c_image=0

def location(event):
    print("x=",event.x,",y=",event.y)
    return 1

def set_win(t_win,w,h,title,color):
    mainsw = int(t_win.winfo_screenwidth() / 2)
    mainsh = int(t_win.winfo_screenheight() / 2)
    t_win.minsize(w, h)
    t_win.maxsize(w, h)
    t_win.geometry(f"1000x600+{mainsw - int(w / 2)}+{mainsh - int(h / 2)}")
    t_win.title(title)
    t_win.config(bg=color)

    return 1

def create_img(contanior,img,w,h):
    img=Image.open(img).resize((w,h))
    imgtk=ImageTk.PhotoImage(img)
    lab=Label(contanior)
    lab.config(image=imgtk,bd=0)
    lab.image=imgtk
    lab.place(x=0,y=0)
    return lab

def change_img(lab):
    try:
        # print("yahan tak a raha ha")
        print(c_image)
        print(images[0])
        imgtk = ImageTk.PhotoImage(images[c_image])
        lab.config(image=imgtk, bd=0)
        lab.image = imgtk
    except:
        print("IN")
    return 1

def browse(lab,lab2,status_lab):
    global total_im
    path=filedialog.askdirectory()
    if path=="":
        pass
    else:
        lab.config(text=path)
        lab.update()
        th=threading.Thread(target=fetch_images,args=(path,status_lab))
        th.start()
        total_im=len(images)
        t=True
        while t:
            total_im=len(images)
            if total_im==0:
                status_lab.config(text="Processing...")
                status_lab.update()
            else:
                t=False
                change_img(lab2)

def fetch_images(path,status_lab):
    for(path,name,farray) in os.walk(path):
        for item in farray:
            s=os.path.splitext(item.lower())
            if s[1] in extensions:
                try:
                    img = Image.open(f"{path}/{item}").resize((700, 400))
                    images.append(img)
                    status_lab.config(text=f"{c_image}/{len(images)}")
                except:
                   print(item)
    messagebox.showinfo("Information","All Image Retrived.......")
    return 1

def rotate(mod,imlab,c_lab,status_lab):
    global c_image
    total_im=len(images)
    if mod==1:
        if c_image==0:
            c_image=total_im-1
        else:
            c_image=c_image-1
            change_img(imlab)
    elif mod==2:
        if c_image == total_im-1:
            # print("Error")
            c_image = 0
        else:
            c_image = c_image + 1

    change_img(imlab)
    status_lab.config(text=f"{c_image+1}/{total_im}")
    return 1
