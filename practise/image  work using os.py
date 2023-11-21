# import os
# os.chdir('C:/Users/JK.tech/Desktop/os image')
# w=os.walk(os.getcwd())
# for current_path,folder_name,file_name in w:
#     print(f"current path :{current_path}")
#     print(f"folder_name : {folder_name}")
#     print(f"file_name : {file_name}")
from PIL import Image
img1=Image.open('C:/Users/JK.tech/Desktop/os image/pics2/pics3/1.png')
img1.show('pic1.jpg')
max_size=(500,500)
img1.thumbnail(max_size)
img1.show()
