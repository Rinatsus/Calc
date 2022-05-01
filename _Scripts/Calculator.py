import tkinter as tk
from Config import *
from Constans import *
import sympy as sym
import ctypes


class Calculator:
    def __init__(self, window):
        self.window = window
        self.operation = ''

        self.window.configure(bg=BACKGROUND_COLOR, bd=BORDER_WIDTH)
        self.window.iconbitmap(ICON_PATH)

        self.input_field = tk.StringVar()
        self.text_field = tk.Entry(self.window, font=('sans-serif', 20, 'bold'), textvariable=self.input_field,
                                   bd=5, insertwidth=5, bg='#BBB', justify='right').grid(row=0, columnspan=10, ipadx=80,
                                                                                         pady=15)
        self.place_buttons()
        self.extend()

    def show(self):
        self.window.mainloop()

    def hide(self):
        self.window.destroy()

    # def equal(self, callback=None):
    #     try:
    #         self.operation = self.get_result()
    #     except Exception:
    #         ctypes.windll.user32.MessageBoxW(0, u"Error", u"Invalid operation", 0)
    #         return
    #
    #     if callback is not None:
    #         callback()

    def clear_all(self):
        self.operation = ''
        self.input_field.set("")

    def clear_one(self):
        self.operation = str(self.operation)[:-1]
        self.input_field.set(self.operation)

    def set_name(self, name):
        self.window.title(name)

    def get_result(self):
        if self.operation == '':
            self.operation = '0'

        temp = sym.sympify(self.operation)
        result = get_int_or_float(temp)
        self.input_field.set(result)
        return result

    def click(self, char: str, val=''):
        if val == '':
            val = char
        self.operation = str(self.operation)
        inp = self.input_field.get()
        if (inp == '0' or inp == '') and char == DOT:
            self.clear_all()
            self.input_field.set(str('0.'))
            self.operation += str('0.')
            return

        if (inp == '0' or inp == '') and CHARS.__contains__(char):
            return

        if inp == '0':
            self.clear_all()

        self.input_field.set(str(self.operation) + char)
        self.operation += str(val)

    def change_sign(self):
        self.operation = str(self.operation)
        if self.operation[0] == '-':
            self.operation = self.operation[1:]
            self.input_field.set(self.operation)
        else:
            self.operation = '-' + self.operation
            self.input_field.set(self.operation)

    def percent(self):
        if self.input_field.get() == '':
            return
        try:
            temp = str(sym.sympify(self.operation + '/100'))
        except Exception:
            ctypes.windll.user32.MessageBoxW(0, u"Error", u"Invalid operation", 0)
            return
        self.operation = temp
        self.get_result()

    def solve(self, action = None):
        if self.operation == '':
            return

        try:
            if action is not None:
                self.operation = action()

            self.operation = self.get_result()
            return self.operation

        except Exception:
            ctypes.windll.user32.MessageBoxW(0, u"Error", u"Invalid operation", 0)

    def square(self):
        self.solve(lambda: str(sym.sympify(self.operation + '**(1/2)')))

    def one_divide(self):
        if self.input_field.get() == '':
            return
        temp = str(sym.simplify(self.operation))
        self.operation = str(sym.sympify('1/' + temp))
        self.get_result()

    def extend(self):
        pass

    def place_buttons(self):
        # row 9
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='0',
                  command=lambda: self.click('0')).grid(row=9, column=2, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text=DOT,
                  command=lambda: self.click(DOT)).grid(row=9, column=3, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='=',
                  command=self.solve).grid(row=9, column=4, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='\u00B1',
                  command=self.change_sign).grid(row=9, column=1, sticky="nsew")

        # row 8
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='1',
                  command=lambda: self.click('1')).grid(row=8, column=1, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='2',
                  command=lambda: self.click('2')).grid(row=8, column=2, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='3',
                  command=lambda: self.click('3')).grid(row=8, column=3, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='+',
                  command=lambda: self.click('+')).grid(row=8, column=4, sticky="nsew")
        # row 7
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='4',
                  command=lambda: self.click('4')).grid(row=7, column=1, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='5',
                  command=lambda: self.click('5')).grid(row=7, column=2, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='6',
                  command=lambda: self.click('6')).grid(row=7, column=3, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='-',
                  command=lambda: self.click('-')).grid(row=7, column=4, sticky="nsew")
        # row 6
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='7',
                  command=lambda: self.click('7')).grid(row=6, column=1, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='8',
                  command=lambda: self.click('8')).grid(row=6, column=2, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='9',
                  command=lambda: self.click('9')).grid(row=6, column=3, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='×',
                  command=lambda: self.click('*')).grid(row=6, column=4, sticky="nsew")

        # row 4
        tk.Button(self.window, CLEAR_BTN_PARAMS,
                  text='C', command=self.clear_one).grid(row=4, column=2, sticky="nsew")
        tk.Button(self.window, CLEAR_BTN_PARAMS,
                  text='CE', command=self.clear_all).grid(row=4, column=3, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='%',
                  command=self.percent).grid(row=4, column=1, sticky="nsew")

        # row 5
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='1/x',
                  command=self.one_divide).grid(row=5, column=1, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='\u00B2\u221A',
                  command=self.square).grid(row=5, column=2, sticky="nsew")
        tk.Button(self.window, NUMBER_BTN_PARAMS, text='/',
                  command=lambda: self.click('/')).grid(row=5, column=3, sticky="nsew")
