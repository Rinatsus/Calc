import tkinter as tk
from Config import *
fro


class Cell(tk.Frame):
    def __init__(self, frame: tk.Frame, text: str):
        super().__init__(frame, bg='#b0afae')
        self.parent = frame
        self.selected = tk.IntVar()
        self.text_result = tk.StringVar()

        self.result = 0
        self.text_result.set(0)

        self.label = tk.Label(self, anchor='w', width=10, bg='#b0afae', textvariable=self.text_result,
                                           font=('sans-serif', 15, 'bold')
                                           ).pack(side='left')
        tk.Checkbutton(self, variable=self.selected).pack(side='left')

    def set(self, val):
        self.result = val
        self.text_result.set(str(self.result))

    def add(self, val):
        self.result += val
        self.text_result.set(str(self.result))

    def substrate(self, val):
        self.result -= val
        self.text_result.set(str(self.result))


class Memory(tk.Frame):
    def __init__(self, window: tk.Tk):
        super().__init__(width=200, bg=BACKGROUND_COLOR)
        self.parent = window
        self.memory_cells = []
        self.grid(row=0, column=10, rowspan=10, sticky='n')

    def add_cell(self, text: str):
        if len(self.memory_cells) < MAX_MEMORY_CELLS:
            cell = Cell(self, text)
            cell.grid(pady=10, sticky="e")
            self.memory_cells.append(cell)

    def add_result(self, val):
        for cell in self.memory_cells:
            if bool(cell.selected.get()):
                cell.add(val)

    def substrate_result(self, val):
        for cell in self.memory_cells:
            if bool(cell.selected.get()):
                cell.substrate(val)
