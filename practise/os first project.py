import os
from PIL import Image
import shutil
os.chdir('C:/Users/JK.tech/Desktop/os image')
w=os.walk(os.getcwd())
for current_path,folder_name,file_name in w:
    os.mkdir('pics2')
    shutil.move('pics','pics2/pics3')
