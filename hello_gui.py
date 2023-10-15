'''This will open up a gui with button 
that will say hello upon clicking the greet button
and keep adding up count as it is clicked.
'''

import tkinter as tk

greeting_count = 1


root = tk.Tk() #use of the Tk class
label = tk.Label(root, text="")

def set_message():
    global greeting_count
    label["text"] = f"Hello! ({greeting_count})"
    greeting_count += 1

#button allows us to create the button that is clickable
button = tk.Button(root, text="Greet", command=set_message)

button.pack()
label.pack()

root.mainloop()


