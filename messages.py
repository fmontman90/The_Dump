"""This is inteded to showcase"""
import tkinter as tk
import sys
from tkinter import messagebox
root = tk.Tk()
root.title("Message_Display")
root.minsize(width=200, height=250)
root.resizable(width=True, height=False)

def display_message(func_name, **kwargs):
    def display():
        #getattr will call the function, and we will return the display
        answer = getattr(sys.modules[messagebox.__name__], func_name)(**kwargs)
        if answer == True:
            print("You clicked something that returned True")
        elif answer == False:
            print("You clicked something that returned False")
        elif answer == "yes":
            print("You clicked something that returned 'yes'")
        elif answer == "no":
            print("You clicked something that returned 'no'")
        elif answer == None:

            print("You clicked something that returned None")
    return display

#Tuples that will return functions
functions = [
 ("askokcancel", messagebox.QUESTION),
 ("askquestion", messagebox.QUESTION),
 ("askretrycancel", messagebox.QUESTION),
 ("askyesno", messagebox.QUESTION),
 ("askyesnocancel", messagebox.QUESTION),
 ("showerror", messagebox.ERROR),
 ("showinfo", messagebox.INFO),
 ("showwarning", messagebox.WARNING),
]

#begin of for loop
for func, icon in functions:
    button = tk.Button(
        root,
        text=f"Display {func}",
        command=display_message(
            func,
            title=f"Rendered {func}",
            message="Message goes here",
            icon=icon,
            detail="Details go here",
        ),
    )
    button.pack()
root.mainloop()