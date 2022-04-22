import tkinter as tk
from Config import *
from Constans import *


class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.operation = ''

        self.configure(bg=BACKGROUND_COLOR, bd=BORDER_WIDTH)
        self.iconbitmap(ICON_PATH)

        self.input_field = tk.StringVar()
        self.text_field = tk.Entry(self, font=('sans-serif', 20, 'bold'), textvariable=self.input_field,
                                   bd=5, insertwidth=5, bg='#BBB', justify='right').grid(columnspan=5, padx=10, pady=15)
        self.place_buttons()

    def show(self):
        self.mainloop()

    def hide(self):
        self.destroy()

    def equal(self):
        temp_op = str(eval(self.operation))
        self.input_field.set(temp_op)
        self.operation = temp_op

    def clear_all(self):
        self.operation = ''
        self.input_field.set("")

    def clear_one(self):
        self.operation = self.operation[:-1]
        self.input_field.set(self.operation)

    def set_name(self, name):
        self.title(name)

    def click(self, char: str):
        self.operation += str(char)
        self.input_field.set(self.operation)

    def change_sign(self):
        if self.operation[0] == '-':
            self.input_field.set(self.operation[1:])
        else:
            self.input_field.set('-' + self.operation)

    def percent(self):
        temp = str(eval(self.operation + '/100'))
        self.operation = temp
        self.input_field.set(temp)

    def square(self):
        if int(self.operation) >= 0:
            temp = str(eval(self.operation + '**(1/2)'))
            self.operation = temp
        else:
            self.operation = "ERROR"

        self.input_field.set(self.operation)

    def one_divide(self):
        temp = str(eval(self.operation))
        self.operation = str(eval('1/' + temp))
        self.input_field.set(self.operation)

    def pow(self, num):
        temp = str(eval(self.operation))
        self.operation = str(pow(float(temp), num))
        self.input_field.set(self.operation)

    def place_buttons(self):
        # row 9
        tk.Button(self, NUMBER_BTN_PARAMS, text='0',
                  command=lambda: self.click('0')).grid(row=9, column=1, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='.',
                  command=lambda: self.click('.')).grid(row=9, column=2, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='=',
                  command=self.equal).grid(row=9, columnspan=2, column=3, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='\u00B1',
                  command=self.change_sign).grid(row=9, column=0, sticky="nsew")


        # row 8
        tk.Button(self, NUMBER_BTN_PARAMS, text='1',
                  command=lambda: self.click('1')).grid(row=8, column=0, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='2',
                  command=lambda: self.click('2')).grid(row=8, column=1, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='3',
                  command=lambda: self.click('3')).grid(row=8, column=2, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='+',
                  command=lambda: self.click('+')).grid(row=8, column=3, sticky="nsew")
        # row 7
        tk.Button(self, NUMBER_BTN_PARAMS, text='4',
                  command=lambda: self.click('4')).grid(row=7, column=0, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='5',
                  command=lambda: self.click('5')).grid(row=7, column=1, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='6',
                  command=lambda: self.click('6')).grid(row=7, column=2, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='-',
                  command=lambda: self.click('-')).grid(row=7, column=3, sticky="nsew")
        # row 6
        tk.Button(self, NUMBER_BTN_PARAMS, text='7',
                  command=lambda: self.click('7')).grid(row=6, column=0, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='8',
                  command=lambda: self.click('8')).grid(row=6, column=1, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='9',
                  command=lambda: self.click('9')).grid(row=6, column=2, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='×',
                  command=lambda: self.click('*')).grid(row=6, column=3, sticky="nsew")

        # row 4
        tk.Button(self, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
                  text='C', command=self.clear_one, bg='#db701f').grid(row=4, column=1, sticky="nsew")
        tk.Button(self, bd=5, fg='#000', font=('sans-serif', 20, 'bold'),
                  text='CE', command=self.clear_all, bg='#db701f').grid(row=4, column=2, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='%',
                  command=self.percent).grid(row=4, column=0, sticky="nsew")

        # row 5
        tk.Button(self, NUMBER_BTN_PARAMS, text='1/x',
                  command=self.one_divide).grid(row=5, column=0, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='x\u00B2',
                  command=lambda:self.pow(2)).grid(row=5, column=1, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='\u00B2\u221A',
                  command=self.square).grid(row=5, column=2, sticky="nsew")
        tk.Button(self, NUMBER_BTN_PARAMS, text='/',
                  command=lambda: self.click('/')).grid(row=5, column=3, sticky="nsew")
