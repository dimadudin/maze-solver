from tkinter import *
from tkinter import ttk


class Cell:
    def __init__(self, x0, y0, x1, y1) -> None:
        self.x0, self.y0 = x0, y0
        self.x1, self.y1 = x1, y1

    def draw_cell(self, canvas):
        canvas.create_line((self.x0, self.y0, self.x0, self.y1))
        canvas.create_line((self.x0, self.y1, self.x1, self.y1))
        canvas.create_line((self.x1, self.y1, self.x1, self.y0))
        canvas.create_line((self.x1, self.y0, self.x0, self.y0))


class Maze:
    def __init__(self, x0, y0, x_num, y_num, cell_size):
        self.cells = [[]]
        cur_x0, cur_y0 = x0, y0
        for _ in range(y_num):
            col = []
            for _ in range(x_num):
                cur_cell = Cell(
                    cur_x0,
                    cur_y0,
                    cur_x0 + cell_size,
                    cur_y0 + cell_size,
                )
                col.append(cur_cell)
                cur_y0 += cell_size
            self.cells.append(col)
            cur_x0 += cell_size
            cur_y0 = y0

    def draw_cells(self, canvas):
        for col in self.cells:
            for cell in col:
                cell.draw_cell(canvas)


root = Tk()
root.title("Maze Solver")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

maze = Maze(100, 100, 10, 10, 100)
maze.draw_cells(canvas)

root.mainloop()
