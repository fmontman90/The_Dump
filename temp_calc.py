import tkinter as tk

class App:
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.temp_value = tk.DoubleVar(self.master, 0.0)
        self.format_value = tk.IntVar(self.master, 0)
        self.calc_on_return = tk.BooleanVar(self.master, True)
        self.calc_on_return.trace("w", self.bind_calc_on_return)

        temp_frame = tk.Frame(self.master)
        temp_frame.pack()
        self.temp_label = tk.Label(temp_frame, text="Temperature:")
        self.temp_label.pack(side="left")
        self.temp_entry = tk.Entry(temp_frame, textvariable=self.temp_value)
        #Example of binding allows for return key to produce result instead of clicking for value
       # self.temp_entry.bind("<Return>", self.convert_temp)
        self.temp_entry.pack(side="right")
        self.bind_calc_on_return()

        format_frame = tk.Frame(self.master)
        format_frame.pack()
        self.format_label = tk.Label(format_frame, text="Output Format:")
        self.format_label.pack(side="left")

        radio_frame = tk.Frame(format_frame)
        radio_frame.pack(side="right")
        #Mistake wit typing used radiobutton all caps led to string errors
        self.format_celsius = tk.Radiobutton(radio_frame, text="Celsius", variable=self.format_value, value=0)
        self.format_celsius.pack(side="left")
        self.format_farh = tk.Radiobutton(radio_frame, text="Farenheit", variable=self.format_value, value=1)
        self.format_farh.pack(side="left")
        #This will allow the user to check whether enter/return can be used to return value
        calc_on_return_checkbox = tk.Checkbutton(
            self.master, text="Calculate on Return/Enter", variable=self.calc_on_return
        )
        calc_on_return_checkbox.pack()

        self.button = tk.Button(self.master, text="Calculate", command=self.convert_temp)
        self.button.pack()
        self.results = tk.Label(self.master)
        self.results.pack()


    def start(self):
        self.master.mainloop()
    
    def convert_temp(self, event=None):
        
        try:
            input_value = self.temp_value.get()
            #added error handler to catch invalid crap!!!
        except tk.TCLError:
            self.results['text'] = "Invalid temperature value"
        else:
            if self.format_value.get() == 0:
                #convert to celsius
                self.results['text'] = f"{round((input_value - 32) * 5 / 9, 2)} C°"
            else:
                #convert to farenheight
                self.results['text'] = f"{round(input_value * 9 / 5 +32, 2)} F°"

    def bind_calc_on_return(self, *args):
        if self.calc_on_return.get():
            self.temp_entry.bind("<Return>", self.convert_temp)
        else:
            self.temp_entry.unbind("<Return>")


if __name__ == "__main__":
    #creation of root object and then rendering it
    root = tk.Tk()
    app = App(root)
    app.start()