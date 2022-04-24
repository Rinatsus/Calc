from Scientific import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


class Plotting(Scientific):
    def __init__(self, window):
        self.x = sym.Symbol('x')
        self.y = sym.Symbol('y')
        self.points_x = []
        self.points_y = []
        self.roots = []
        super(Plotting, self).__init__(window)
        self.set_name(NAME + PLOTTING)

        self.fig, self.ax = plt.subplots()
        self.ax.minorticks_on()
        self.ax.grid(which='minor',
                     color='k',
                     linestyle=':')

        axis = plt.gca()
        axis.axhline(y=0, color='k')
        axis.axvline(x=0, color='k')

        self.show_plot()

    def equal(self, callback=None):
        self.points_x = []
        self.operation = get_formatted_expression(self.operation)
        self.input_field.set(self.operation)
        self.roots = sym.solve(sym.Eq(self.operation, 0), self.x)
        self.roots = sorted(self.roots)

        for i in range(len(self.roots) - 1):
            self.points_x = np.r_[self.points_x,
                                  np.linspace(float(self.roots[i].n()), float(self.roots[i + 1].n()), 20)]
        self.points_y = get_points(self.points_x, self.operation)

        self.show_plot()

        print(self.roots)

    def place_memory(self):
        pass

    def hide(self):
        plt.close()
        super(Plotting, self).hide()

    def show_plot(self):
        self.ax.plot(self.points_x, self.points_y)
        # specify the window as master
        canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, rowspan=10, column=10, padx=10, ipadx=40, ipady=20)

        # navigation toolbar
        toolbarFrame = tk.Frame(master=self.window)
        toolbarFrame.grid(row=10, column=10)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

    def extend(self):
        super(Plotting, self).extend()
        tk.Button(self.window, PLOTTING_BTN_PARAMS, text=f"{self.x}",
                  command=lambda: self.click(f"{self.x}")).grid(row=2, column=4, sticky="nsew")
        tk.Button(self.window, PLOTTING_BTN_PARAMS, text=f"{self.y}",
                  command=lambda: self.click(f"{self.y}")).grid(row=3, column=4, sticky="nsew")
        tk.Button(self.window, PLOTTING_BTN_PARAMS, text='=',
                  command=lambda: self.click('=')).grid(row=4, column=4, sticky="nsew")
