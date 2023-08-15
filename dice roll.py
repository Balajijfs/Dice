
'''import random

dice=[1,2,3,4,5,6]

print(random.choice(dice))
print(random.choice(dice))'''



import tkinter as tk
import random

root=tk.Tk()

root.title("Dice Roll")
root.geometry("700x450")
root.resizable(False,False)


label=tk.Label(root,text="",font=("times",260))

def roll():
    dice=["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()

button=tk.Button(root,text="Let's Play",width=40,height=3,font=("Arial",10),bg="#fe9037",fg="white",command=roll)

button.pack(padx=15,pady=15)

root.mainloop()