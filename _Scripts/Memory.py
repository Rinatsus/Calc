import tkinter as tk
from Config import *
from Constans import *
import os.path


class Cell(tk.Frame):
    def __init__(self, frame: tk.Frame, val: str, name):
        super().__init__(frame, bg='#b0afae')
        self.name = name
        self.parent = frame
        self.selected = tk.IntVar()
        self.text_result = tk.StringVar()
        print(val)
        self.result = val
        self.text_result.set(self.result)

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
        self.data = Data()
        self.load()

    def add_cell(self, val):
        if len(self.memory_cells) < MAX_MEMORY_CELLS:
            cell = Cell(self, get_int_or_float(val), len(self.memory_cells))
            cell.grid(pady=10, sticky="e")
            self.memory_cells.append(cell)
            self.data.append(cell.name, cell.result)
            self.save()

    def add_result(self, val):
        for cell in self.memory_cells:
            if bool(cell.selected.get()):
                cell.add(val)
                self.data.append(cell.name, cell.result)
        self.save()

    def substrate_result(self, val):
        for cell in self.memory_cells:
            if bool(cell.selected.get()):
                cell.substrate(val)
                self.data.append(cell.name, cell.result)
        self.save()

    def save(self):
        with open(DATA_PATH, 'w') as file:
            file.write("{")
            for key, val in self.data.results.items():
                file.write('{}:{},'.format(key, val))
            file.write("}")

    def load(self):
        if os.path.exists(DATA_PATH) == False:
            return

        with open(DATA_PATH, 'r') as file:
            try:
                self.data.results = eval(file.readline())
            except Exception:
                return

            for name, result in self.data.results.items():
                self.add_cell(result)



class Data:
    def __init__(self):
        self.results = {}

    def set(self, results):
        self.results = results

    def append(self, name, result):
        self.results[name] = result
