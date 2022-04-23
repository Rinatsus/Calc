from Common import *
from Scientific import *
import tkinter as tk


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.activeCalc = ''
        self.place_menu()
        self.show_scientific()

    def show_common(self):
        self.close_last()

        self.activeCalc = Common(self.window)
        self.show_new()

    def show_scientific(self):
        self.close_last()

        self.activeCalc = Scientific(self.window)
        self.show_new()

    def close_last(self):
        if self.activeCalc != '':
            self.activeCalc.hide()
            self.window = tk.Tk()
            self.place_menu()

    def show_new(self):
        if self.activeCalc != '':
            self.activeCalc.show()
            self.window = tk.Tk()

    def place_menu(self):
        menu = tk.Menu(self.window)
        file_menu = tk.Menu(menu, tearoff=0)

        file_menu.add_command(label="Scientific", command=self.show_scientific)
        file_menu.add_command(label="Common", command=self.show_common)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.destroy)
        menu.add_cascade(label="Mode", menu=file_menu)
        self.window.config(menu=menu)
