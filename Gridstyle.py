#Gridstyle layout
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1", bg="blue")
label1.grid(column=1,row=1, ipadx=30, ipady=30)


label2 = tk.Label(root, text="Label 2", bg="red")
label2.grid(column= 2, row=1, ipadx=30, ipady=30)

label3 = tk.Label(root, text="Label 3", bg="green")
label3.grid(sticky=tk.E + tk.W, columnspan=3, ipadx=30, ipady=30)

root.mainloop()