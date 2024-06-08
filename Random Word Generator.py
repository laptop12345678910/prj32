from tkinter import *
import random

root  = Tk()
root.title("Random Word Generator")
root.geometry("400x400")
root.configure(background = "light blue")

label1 = Label(root)

def Generate():
    alpha_list["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random_no1.randint(1,26)
    print(random_no1)
    random_no2.randint(1,26)
    print(random_no2)
    random_no3.randint(1,26)
    print(random_no3)
    random_no4.randint(1,26)
    print(random_no4)
    random_no5.randint(1,26)
    print(random_no5)
    
    random1 = alpha_list[random_no1]
    random2 = alpha_list[random_no2]
    random3 = alpha_list[random_no3]
    random4 = alpha_list[random_no4]
    random5 = alpha_list[random_no5]
    
label1["text"] += random1 + random2 + random3 + random4 + random5
label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn = Button(root, text = "Generate Random Number", command = Generate)
btn.place(relx = 0.5, rely = 0.6)

root.mainloop()