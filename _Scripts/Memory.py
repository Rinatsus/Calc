import tkinter as tk
from Config import *
from Constans import *
import os


class Cell(tk.Frame):
    def __init__(self, frame: tk.Frame, val: str, name):
        super().__init__(frame, bg='#b0afae')
        self.name = name
        self.parent = frame
        self.selected = tk.IntVar()
        self.text_result = tk.StringVar()
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

    def clear(self):
        self.result = 0
        self.text_result.set('0')


class Memory(tk.Frame):
    def __init__(self, window: tk.Tk, menu: tk.Menu):
        super().__init__(width=200, bg=BACKGROUND_COLOR)
        self.parent = window
        self.memory_cells = []
        self.grid(row=0, column=10, rowspan=10, sticky='n')
        self.data = Data()
        self.load()
        self.menu = menu
        self.place_menu()

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
                cell.add(get_int_or_float(val))
                self.data.append(cell.name, cell.result)
        self.save()

    def substrate_result(self, val):
        for cell in self.memory_cells:
            if bool(cell.selected.get()):
                cell.substrate(val)
                self.data.append(cell.name, cell.result)
        self.save()

    def save(self):
        if not os.path.exists(DIR_DATA_PATH):
            os.mkdir(DIR_DATA_PATH)

        with open(SCIENTIFIC_DATA_PATH, 'w') as file:
            file.write("{")
            for key, val in self.data.results.items():
                file.write('{}:{},'.format(key, val))
            file.write("}")

    def load(self):
        if not os.path.exists(SCIENTIFIC_DATA_PATH):
            return

        with open(SCIENTIFIC_DATA_PATH, 'r') as file:
            try:
                self.data.results = eval(file.readline())
            except Exception:
                return
            copyData = self.data.results.copy()
            for name, result in copyData.items():
                self.add_cell(result)

    def delete(self, selected=False):
        if not os.path.exists(SCIENTIFIC_DATA_PATH):
            return

        cells = self.memory_cells.copy()

        if selected:
            for cell in cells:
                if bool(cell.selected.get()):
                    self.data.remove(cell.name)
                    self.memory_cells.remove(cell)
                    cell.destroy()
            os.remove(SCIENTIFIC_DATA_PATH)
            self.save()
        else:
            for cell in cells:
                self.data.remove(cell.name)
                self.memory_cells.remove(cell)
                cell.destroy()
            os.remove(SCIENTIFIC_DATA_PATH)

    def clear(self, selected=False):
        if selected:
            for cell in self.memory_cells:
                if bool(cell.selected.get()):
                    cell.clear()
        else:
            for cell in self.memory_cells:
                cell.clear()


    def place_menu(self):
        memory_menu = tk.Menu(self.menu, tearoff=0)
        memory_menu.add_command(label="Delete", command=self.delete)
        memory_menu.add_command(label="Clear", command=self.clear)
        memory_menu.add_separator()
        memory_menu.add_command(label="DeleteSelected", command=lambda: self.delete(True))
        memory_menu.add_command(label="ClearSelected", command=lambda: self.clear(True))
        self.menu.add_cascade(label="Memory", menu=memory_menu)


class Data:
    def __init__(self):
        self.results = {}

    def set(self, results):
        self.results = results

    def append(self, name, result):
        self.results[name] = result

    def remove(self, key):
        self.results.pop(key)
