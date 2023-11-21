import os
from tkinter import filedialog
#
# w=os.walk("")
path=filedialog.askdirectory()
extensions=('.png','.jpg')
extensions2=('.mp4')
for path,folder_name,file_name in os.walk(path):
#     print(f"folder Name : { folder_name}")
#     print(f"file_name : {file_name}")

    for i in file_name:
        temp = os.path.splitext(i.lower())
        if temp[1] in extensions:
                print(i)
        if temp[1] in extensions2:
            print(f"Its Video : {i}")
