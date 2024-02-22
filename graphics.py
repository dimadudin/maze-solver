from tkinter import Tk, Canvas, N, W, E, S
import time


class Window:
    def __init__(self, width, height) -> None:
        self.w, self.h = width, height
        self.__root = Tk()
        self.__root.geometry(f"{self.w}x{self.h}")
        self.__root.title("Maze Solver")
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)

        self.__canvas = Canvas(self.__root)
        self.__canvas.grid(column=0, row=0, sticky=(N, W, E, S))

    def start_maze(self, row_n, col_m):
        cell_size = min(self.w // (row_n + 2), self.h // (col_m + 2))
        x0, y0 = cell_size, cell_size
        maze = Maze(Point(x0, y0), row_n, col_m, cell_size, self)
        maze.draw_cells()

        self.__root.mainloop()

    def draw_line(self, *args, **kwargs):
        self.__canvas.create_line(*args, **kwargs)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def mainloop(self):
        self.__root.mainloop()


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p0, p1, fill="black") -> None:
        self.p0 = p0
        self.p1 = p1
        self.fill = fill

    def draw(self, window):
        window.draw_line(
            self.p0.x, self.p0.y, self.p1.x, self.p1.y, fill=self.fill, width=4
        )


class Cell:
    def __init__(self, p0, p1) -> None:
        self.tl, self.bl = Point(p0.x, p0.y), Point(p0.x, p1.y)
        self.br, self.tr = Point(p1.x, p1.y), Point(p1.x, p0.y)
        self.lb, self.bb = True, True
        self.rb, self.tb = True, True
        self.visited = False

    def draw(self, window):
        colors = []
        for border in [self.lb, self.bb, self.rb, self.tb]:
            if border is True:
                colors.append("black")
            else:
                colors.append("#D9D9D9")

        Line(self.tl, self.bl, fill=colors[0]).draw(window)
        Line(self.bl, self.br, fill=colors[1]).draw(window)
        Line(self.br, self.tr, fill=colors[2]).draw(window)
        Line(self.tr, self.tl, fill=colors[3]).draw(window)
        window.redraw()
        time.sleep(0.0075)


class Maze:
    def __init__(self, p0, row_n, col_m, cell_size, window=None):
        self.cells = self._create_cells(p0, row_n, col_m, cell_size)
        self.window = window

    def _create_cells(self, p0, row_n, col_m, cell_size):
        curr_p0 = Point(p0.x, p0.y)
        curr_p1 = Point(p0.x + cell_size, p0.y + cell_size)
        cols = []
        for _ in range(col_m):
            col = []
            for _ in range(row_n):
                curr_cell = Cell(curr_p0, curr_p1)
                col.append(curr_cell)
                curr_p0.y += cell_size
                curr_p1.y += cell_size
            cols.append(col)
            curr_p0.x += cell_size
            curr_p0.y = p0.y
            curr_p1.x = curr_p0.x + cell_size
            curr_p1.y = curr_p0.y + cell_size
        return cols

    def draw_cells(self):
        for col in self.cells:
            for cell in col:
                cell.draw(self.window)

    def break_st_end(self):
        self.cells[0][0].tb = False
        self.cells[-1][-1].bb = False
        self.draw_cells()

    def break_walls(self):
        pass
