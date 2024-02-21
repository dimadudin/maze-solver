from tkinter import *
from tkinter import ttk


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")

        self.__mainframe = ttk.Frame(self.__root, width=width, height=height).grid()

    def mainloop(self):
        self.__root.mainloop()
