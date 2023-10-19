import tkinter as tk
from tkinter import *
import itertools


class Calculator:
    def __init__(self, width=500, height=500):
        self.width = width
        self.height = height
        self.window = Tk()
        self.window.geometry(f'{self.width}x{self.height}')
        self.display = tk.Entry(self.window).grid(row=0, column=0, columnspan=3)
        self.number_buttons = self._buttons_of_numbers()

    def _buttons_of_numbers(self):
        number_buttons = []
        index = 1
        for row, column in itertools.product('123', '012'):
            # self.window.rowconfigure(row, weight=1)
            # self.window.columnconfigure(column, weight=1)
            btn = tk.Button(self.window, text=f'{index}', width=5, height=3)
            btn.grid(row=row, column=column)
            number_buttons.append(btn)
            index += 1
        btn = tk.Button(self.window, text=0)
        btn.grid(row=5, column=0)
        number_buttons.append(btn)
        return number_buttons


def main():
    calculator = Calculator()
    calculator.window.mainloop()


if __name__ == '__main__':
    main()
