#This is meant to show th gui pack style
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1", bg="blue")
label1.pack(ipadx=30, ipady=30)
#Example of some fill ins
#side=tk.LEFT, fill=None, expand=False, anchor=tk.NW
#fill.tk.BOTH, expand=True

label2 = tk.Label(root, text="Label 2", bg="red")
label2.pack(ipadx=30, ipady=30, side=tk.LEFT)

label3 = tk.Label(root, text="Label 3", bg="green")
label3.pack(ipadx=30, ipady=30, side=tk.RIGHT)

root.mainloop()