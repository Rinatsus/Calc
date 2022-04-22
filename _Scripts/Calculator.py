import tkinter as tk
from Config import *


class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.operation = ''

        self.configure(bg=BACKGROUND_COLOR, bd=BORDER_WIDTH)
        self.iconbitmap(ICON_PATH)

        self.input_field = tk.StringVar()
        self.text_field = tk.Entry(self, font=('sans-serif', 20, 'bold'), textvariable=self.input_field,
                     bd=5, insertwidth = 5, bg='#BBB', justify='right').grid(columnspan=5, padx = 10, pady = 15)
        self.place_buttons()


    def hide(self):
        self.destroy()

    def equal(self):
        temp_op = str(eval(self.operation))
        self.input_field.set(temp_op)
        self.operation = temp_op

    def clear_all(self):
        self.operation = ''
        self.input_field.set("")

    def delete(self):
        self.operation = self.operation[:-1]
        self.input_field.set(self.operation)

    def set_name(self, name):
        self.title(name)

    def click(self, char: str):
        self.operation += str(char)
        self.input_field.set(self.operation)

    def place_buttons(self):
        # row 9
        tk.Button(self, NUMBER_BTN_PARAMS, text='0',
                  command=lambda: self.click('0')).grid(row=9, column=1, sticky="nsew")
        # row 8
        tk.Button(self, NUMBER_BTN_PARAMS, text='1',
                  command=lambda: self.click('1')).grid(row=8, column=0, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='2',
                  command=lambda: self.click('2')).grid(row=8, column=1, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='3',
                  command=lambda: self.click('3')).grid(row=8, column=2, sticky="nsew")

        # row 7
        tk.Button(self, NUMBER_BTN_PARAMS, text='4',
                  command=lambda: self.click('4')).grid(row=7, column=0, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='5',
                  command=lambda: self.click('5')).grid(row=7, column=1, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='6',
                  command=lambda: self.click('6')).grid(row=7, column=2, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='7',
                  command=lambda: self.click('7')).grid(row=6, column=0, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='8',
                  command=lambda: self.click('8')).grid(row=6, column=1, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='9',
                  command=lambda: self.click('9')).grid(row=6, column=2, sticky="nsew")
