#!/usr/bin/python3

from tkinter import *
from tkinter import ttk, END

class App:
    
    def __init__(self, master):
        self.label = ttk.Label(master, text = "Time Converter", font = ["Simplo", 18, "bold"])
        self.label.grid(row = 0, column = 0, columnspan = 2)
        self.label.config(justify = CENTER)

        self.entry_widget = ttk.Entry(master)
        self.entry_widget.grid(row = 2, column = 0)

        R1 = ttk.Radiobutton(master, text = "24hr to 12hr", value = 1).grid(row = 2, column = 1)
        R2 = ttk.Radiobutton(master, text = "12hr to 24hr", value = 2).grid(row = 3, column = 1)

        action_button = ttk.Button(master, text = "Calculate", command = self.get_entry_data).grid(row = 3, column = 0)

    def get_entry_data(self):
        data = self.entry_widget.get()

        self.entry_widget.delete(0, END)
        
        return print(str(data))

def main():

    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__": main()
