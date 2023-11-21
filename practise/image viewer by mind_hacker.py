import virtual_code
from virtual_code import *
class frontend:
    def ist_win(self):
        win=Tk()
        set_win(win,1000,600,"Advance Image Viewer","gray")
        main_fram=Frame(win,bg="#2b2b2b",width=700,height=400)
        main_fram.place(x= 150 ,y= 40)
        labim=create_img(main_fram,"C:/Users/JK.tech/OneDrive/Desktop/IMG-20230324-WA0032.jpg",700,400)

        count_lab = Label(win, text="",height=1,width=6 ,font=("forte", 20),bg="white", fg="Red")
        count_lab.place(x=445, y=537)
        lab=Label(win,text="Select Source Folder . . .",font=("Arial",12),bg="gray",fg="white")
        lab.place(x= 203 ,y= 461)
        t_lab=Label(win,text="-----/-----",font=("forte,12"),bg="gray",fg="white")
        t_lab.place(x=500,y=10)
        Button(win,text="Browse",bg="#ffffff",font=("forte",13),width="10",command=lambda :browse(lab,labim,t_lab)).place(x= 675 ,y= 460)
        Button(win,text="Previous",bg="#ffffff",font=("forte",15),width="20",command=lambda :rotate(1,labim,count_lab,t_lab)).place(x= 200 ,y= 537)
        Button(win,text="Next",bg="#ffffff",font=("forte",15),width="20",command=lambda :rotate(2,labim,count_lab,t_lab)).place(x= 560 ,y= 537)


        win.bind("<Button-1>",lambda event:location(event))
        win.mainloop()
        return 1

obj=frontend()
obj.ist_win()
