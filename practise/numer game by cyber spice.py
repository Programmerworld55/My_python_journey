print("\n\n\t\t..........     Number Game By Cyber Spice     ..........")
number=int(input("\n\t\t  ..........        Enter  Any Number : "))

r_num=0
w_num=17
while True:
    if number==w_num:
        r_num+=1
        print("\n\t\t.........            YOU WIN                 ..........")
        break
    if number < w_num:
        print("\n\t  ..........          Tooo Low               ...........")
        number = int(input("\n\n\t..........     Enter Number Again : "))
        r_num += 1
    if number > w_num:
        print("\n\t  ..........          Tooo HIGH               ...........")
        number = int(input("\n\n\t..........     Enter Number Again : "))
        r_num += 1
print("\n\n\t\tYou Guess This Number ",r_num,"Time")

