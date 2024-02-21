from tkinter import *
from tkinter import ttk


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")

        self.__mainframe = ttk.Frame(self.__root, padding="100 100 10 10")
        self.__mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)

        ttk.Label(self.__mainframe, text="THIS IS TEXT").grid(column=1, row=1, sticky=W)

    def mainloop(self):
        self.__root.mainloop()
