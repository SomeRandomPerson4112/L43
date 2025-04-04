from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.title("Password Strength Checker")

lbl = Label(text="Please write your password", fg="black")
entry = Entry()

def password():
    pwd = entry.get()
    length = len(pwd)
    
    if length <= 5:
        messagebox.showinfo("Password Strength", "Your password is weak")
    elif 6 <= length <= 8:
        messagebox.showinfo("Password Strength", "Your password is medium strength")
    elif 9 <= length <= 12:
        messagebox.showinfo("Password Strength", "Your password is strong")
    else:
        messagebox.showinfo("Password Strength", "Your password is very strong")

btn = Button(text="Enter", bg="red", fg="white", command=password)

lbl.pack()
entry.pack()
btn.pack()

root.mainloop()
