from Scientific import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import os


class Plotting(Calculator):
    def __init__(self, window, menu: tk.Menu):
        self.x = sym.Symbol('x')
        self.menu = menu
        self.points_x = []
        self.points_y = []
        self.roots = []
        super(Plotting, self).__init__(window)
        self.set_name(NAME + PLOTTING)
        self.figure, self.plot_axis = plt.subplots()
        self.place_menu()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.window)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, rowspan=10, column=10, padx=10, ipadx=40, ipady=20)

        toolbarFrame = tk.Frame(master=self.window)
        toolbarFrame.grid(row=10, column=10)
        NavigationToolbar2Tk(self.canvas, toolbarFrame)

        self.draw_axis()

    def solve(self, callback=None):
        try:
            self.operation = get_formatted_expression(self.operation)
        except Exception:
            ctypes.windll.user32.MessageBoxW(0, u"Error", u"Invalid operation", 0)
            return

        self.points_x = []
        self.input_field.set(self.operation)
        self.roots = sym.solve(sym.Eq(self.operation, 0), self.x)
        if len(self.roots) > 0:
            if self.roots[0] != 0 and len(self.roots) == 1:
                self.roots.append(0)
        else:
            return

        for i in range(len(self.roots)):
            self.roots[i] = get_int_or_float(self.roots[i])

        self.roots = sorted(self.roots)

        for i in range(len(self.roots) - 1):
            r1 = self.roots[i]
            r2 = self.roots[i + 1]

            self.points_x = np.r_[self.points_x,np.linspace(r1, r2, ACCUARY)]

        self.points_y = interpolate(self.points_x, self.operation)
        self.show_plot()

    def draw_axis(self):
        self.plot_axis.clear()
        self.plot_axis.minorticks_on()
        self.plot_axis.grid(which='minor',
                            color='k',
                            linestyle=':')

        axis = plt.gca()
        axis.axhline(y=0, color='k')
        axis.axvline(x=0, color='k')


    def show_plot(self):
        self.plot_axis.plot(self.points_x, self.points_y)
        self.canvas.draw()

    def extend(self):
        tk.Button(self.window, PLOTTING_BTN_PARAMS, text=f"{self.x}",
                  command=lambda: self.click(f"{self.x}")).grid(row=4, column=4, sticky="nsew")
        tk.Button(self.window, PLOTTING_BTN_PARAMS, text='=',
                  command=lambda: self.click('=')).grid(row=5, column=4, sticky="nsew")

        # row 2
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="sin(n)",
                  command=lambda: self.click('sin(')).grid(row=2, column=1, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="cos(n)",
                  command=lambda: self.click('cos(')).grid(row=2, column=2, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="tan(n)",
                  command=lambda: self.click('tan(')).grid(row=2, column=3, sticky="nsew")

        # row 3
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="(",
                  command=lambda: self.click('(')).grid(row=3, column=2, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text=")",
                  command=lambda: self.click(')')).grid(row=3, column=3, sticky="nsew")

        # row 8
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="ln(n)",
                  command=lambda: self.click('ln(')).grid(row=2, column=4, sticky="nsew")

        # row 7
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="log(n)",
                  command=lambda: self.click('log(')).grid(row=3, column=4, sticky="nsew")

        # row 6
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text="n\u1D61",
                  command=lambda: self.click('**')).grid(row=5, column=1, sticky="nsew")
        tk.Button(self.window, SCIENTIFIC_BTN_PARAMS, text=PI,
                  command=lambda: self.click(PI, f"{pi}")).grid(row=3, column=1, sticky="nsew")

    def clear(self):
        self.plot_axis.clear()
        self.draw_axis()
        self.canvas.draw()

    def load(self):
        if not os.path.exists(PLOT_DATA_PATH):
            return

        with open(PLOT_DATA_PATH, 'r') as file:
            self.operation = file.readline()
            self.input_field.set(self.operation)
            self.solve()

    def save(self):
        if not os.path.exists(DIR_DATA_PATH):
            os.mkdir(DIR_DATA_PATH)

        with open(PLOT_DATA_PATH, 'w') as file:
            file.write(str(self.operation))

    def delete(self):
        if not os.path.exists(PLOT_DATA_PATH):
            return

        os.remove(PLOT_DATA_PATH)
        self.clear()

    def place_menu(self):
        plot_menu = tk.Menu(self.menu, tearoff=0)
        plot_menu.add_command(label="SaveLast", command=self.save)
        plot_menu.add_command(label="LoadLast", command=self.load)
        plot_menu.add_separator()
        plot_menu.add_command(label="Delete", command=self.delete)
        plot_menu.add_command(label="Clear", command=self.clear)
        self.menu.add_cascade(label="Plot", menu=plot_menu)
        self.window.config(menu=self.menu)
