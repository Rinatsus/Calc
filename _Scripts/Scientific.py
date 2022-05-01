from Calculator import *
from Memory import *


class Scientific(Calculator):
    def __init__(self, window: tk.Tk, menu):
        super(Scientific, self).__init__(window)
        self.set_name(NAME + SCIENTIFIC)
        self.place_memory(menu)

    def solve_sin(self):
        self.solve(lambda: str(sin(sym.sympify(self.operation))))

    def solve_cos(self):
        self.solve(lambda: str(cos(sym.sympify(self.operation))))

    def solve_tan(self):
        self.solve(lambda: str(tan(sym.sympify(self.operation))))


    def solve_factorial(self):
        self.solve(lambda: str(fac(sym.simplify(self.operation))))

    def pow(self, num):
        self.solve(lambda: str(pow(eval(self.operation), num)))

    def solve_ten_in_pow(self):
        self.solve(lambda: str(pow(10, sym.sympify(self.operation))))

    def solve_ln(self):
        self.solve(lambda: str(ln(sym.sympify(self.operation))))

    def solve_log10(self):
        self.solve(lambda: str(log(sym.sympify(self.operation))))

    def solve_abs(self):
        self.solve(lambda: str(abs(sym.sympify(self.operation))))

    def solve_exp(self):
        self.solve(lambda: str(exp(sym.sympify(self.operation))))

    def add_memory_cell(self):
        value = '0' if self.operation == '' else sym.sympify(self.operation)
        self.memory.add_cell(value)

    def place_memory(self, menu: tk.Menu):
        self.memory = Memory(self.window, menu)
        tk.Button(self.window, MEMORY_BTN_PARAMS, text='M+',
                  command=lambda: self.memory.add_result(self.get_result())).grid(row=2, column=4, sticky="nsew")
        tk.Button(self.window, MEMORY_BTN_PARAMS, text='M-',
                  command=lambda: self.memory.substrate_result(self.get_result())).grid(row=3, column=4, sticky="nsew")
        tk.Button(self.window, MEMORY_BTN_PARAMS, text='M',
                  command=self.add_memory_cell).grid(row=4, column=4, sticky="nsew")

    def extend(self):
        # row 2
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="sin(n)",
                  command=self.solve_sin).grid(row=2, column=1, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="cos(n)",
                  command=self.solve_cos).grid(row=2, column=2, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="tan(n)",
                  command=self.solve_tan).grid(row=2, column=3, sticky="nsew")

        # row 3
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="(",
                  command=lambda: self.click('(')).grid(row=3, column=2, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text=")",
                  command=lambda: self.click(')')).grid(row=3, column=3, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="n!",
                  command=self.solve_factorial).grid(row=3, column=1, sticky="nsew")

        # row 9
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="10\u207F",
                  command=self.solve_ten_in_pow).grid(row=9, column=0, sticky="nsew")

        # row 8
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="ln(n)",
                  command=self.solve_ln).grid(row=8, column=0, sticky="nsew")

        # row 7
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="log(n)",
                  command=self.solve_log10).grid(row=7, column=0, sticky="nsew")

        # row 6
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="n\u1D61",
                  command=lambda: self.click('**')).grid(row=6, column=0, sticky="nsew")
        # row 5
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="n\u00B2",
                  command=lambda: self.pow(2)).grid(row=5, column=0, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text=PI,
                  command=lambda: self.click(PI, f"{pi}")).grid(row=5, column=4, sticky="nsew")

        # row 4
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="e",
                  command=lambda: self.click('e', f"{e}")).grid(row=4, column=0, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="e",
                  command=lambda: self.click('e', f"{e}")).grid(row=4, column=0, sticky="nsew")
        # row 3
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="exp",
                  command=self.solve_exp).grid(row=3, column=0, sticky="nsew")

        # row 2
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text='|x|',
                  command=self.solve_abs).grid(row=2, column=0, sticky="nsew")
