#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

class App:
    
    def __init__(self, master):
        self.label = ttk.Label(master, text = "Welcome!!", font = ["Simplo", 18, "bold"])
        self.label.grid(row = 0, column = 0, columnspan = 2)
        self.label.config(justify = CENTER)

        button1 = ttk.Button(master, text = "Banana", command = self.banana).grid(row = 1, column = 0)
        button2 = ttk.Button(master, text = "BlueBerry", command = self.blueberry).grid(row = 1, column = 1)

    def banana(self):
        banana = PhotoImage(file = "C:\\Users\\Zach\\Desktop\\RandomPractice\\TKinter\\Fruits\\banana.gif")
        self.label.config(text = "The banana is a long yellow fruit. It grows on trees and monkies love them! If you want to know more about bananas, visit bananatime.org")
        self.label.config(wraplength = 240)
        self.label.config(foreground = "yellow", background = "black")
        self.label.img = banana
        self.label.config(image = self.label.img)
        self.label.config(compound = "left")
        
    def blueberry(self):
        blueberry = PhotoImage(file = "C:\\Users\\Zach\\Desktop\\RandomPractice\\TKinter\\Fruits\\blueberries.gif")
        self.label.config(text = "The blueberry is a small blue berry found in the wild. Double check you're eating the right one! You can easily confuse them for poisonious berries!")
        self.label.config(wraplength = 240)
        self.label.config(foreground = "blue", background = "black")
        self.label.img = blueberry
        self.label.config(image = self.label.img)
        self.label.config(compound = "left")

def main():

    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__": main()
