import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def display_pop():
    messagebox.showinfo(
        title= "Success",
        message="Successfully displayed popup"
    )

button = tk.Button(
    root,
    text="Display Popup",
    command=display_pop
)

button.pack()

root.mainloop()