import os
# print(os.getcwd())
# os.mkdir('extra')
# print(os.path.exists('movies'))
# open('file.txt','a').close()
# os.mkdir('C:/Users/JK.tech/Desktop/viruses/movies')
# print(os.listdir('C:/Users/JK.tech/Desktop/viruses'))
os.chdir('C:/Users/JK.tech/Desktop/HIDE')
print(os.listdir())

# import shutil
# # os.mkdir('extra2')
# shutil.move('H:\PC DATA\python all programs\extra\os_extra.txt','extra2/os2.py')
w=os.walk(os.getcwd())
for current_path,folder_name,file_name in w:
    print(f"current path : {current_path}")
    print(f"folder_name : {folder_name}")
    print(f"file_name : {file_name}")