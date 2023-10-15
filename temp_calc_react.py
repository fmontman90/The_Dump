#This alter is for reactive over the first mmodel we created.
import tkinter as tk

class App:
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.temp_value = tk.DoubleVar(self.master, 0.0)
        self.format_value = tk.IntVar(self.master, 0)
        self.result_value = tk.StringVar(self.master)

        self.temp_value.trace("w", self.convert_temp)
        self.format_value.trace("w", self.convert_temp)

        temp_frame = tk.Frame(self.master)
        temp_frame.pack()
        self.temp_label = tk.Label(temp_frame, text="Temperature:")
        self.temp_label.pack(side="left")
        self.temp_entry = tk.Entry(temp_frame, textvariable=self.temp_value)
        self.temp_entry.pack(side="right")

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

        self.results = tk.Label(self.master, textvariable=self.result_value)
        self.results.pack()
        self.convert_temp()

    ''' This was used in the initial format to quick fill
        self.temp_label.pack()
        self.temp_entry.pack()
        self.format_label.pack()
        self.format_celsius.pack()
        self.format_farh.pack()
        self.button.pack()
        self.results.pack() '''



    def start(self):
        self.master.mainloop()
    
    def convert_temp(self, *args):
        try:
            input_value = self.temp_value.get()
        except tk.TCLError:
            self.result_value.set("Invalid temperature value")
        else:
            if self.format_value.get() == 0:
                #convert to celsius
                self.result_value.set(f"{round((input_value - 32) * 5 / 9, 2)} C")
            else:
                #convert to farenheight
                self.result_value.set(f"{round(input_value * 9 / 5 +32, 2)} F")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.start()