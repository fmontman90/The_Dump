
import tkinter as tk


root = tk.Tk()

root.title("My Window")
#root.iconphoto(True, tk.PhotoImage(file="icon.png"))
root.geometry("500x300+200+200")

root.minsize(width=1000, height=300)
root.maxsize(width=1000, height=400)
root.resizable(width=True, height=True)

button = tk.Button(
    root,
    background="#FF0000",
    activebackground="#FF0000",
    foreground="#00FF00",
    text="Press Me",
    activeforeground="#0000FF"

)
button.pack(padx=30, pady=30)


root.mainloop()