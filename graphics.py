from tkinter import Tk, Canvas, N, W, E, S
import random
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
            if border:
                colors.append("black")
            else:
                colors.append("#D9D9D9")

        Line(self.tl, self.bl, fill=colors[0]).draw(window)
        Line(self.bl, self.br, fill=colors[1]).draw(window)
        Line(self.br, self.tr, fill=colors[2]).draw(window)
        Line(self.tr, self.tl, fill=colors[3]).draw(window)


class Maze:
    def __init__(self, p0, row_n, col_n, cell_size, window=None, seed=None):
        self._row_n, self._col_n = row_n, col_n
        self._cells = self._create_cells(p0, row_n, col_n, cell_size)
        self.window = window
        if seed:
            random.seed(seed)
        self._draw_cells()
        self.break_st_end()
        self._break_walls_r(0, 0)

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

    def _draw_cells(self):
        for col in self._cells:
            for cell in col:
                cell.draw(self.window)
                self._animate()

    def _draw_cell(self, i, j):
        self._cells[i][j].draw(self.window)
        self._animate()

    def _animate(self):
        if self.window:
            self.window.redraw()
        time.sleep(0.02)

    def break_st_end(self):
        self._cells[0][0].tb = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].bb = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self._col_n - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self._row_n - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if not to_visit:
                self._draw_cell(i, j)
                return

            next_index = random.choice(to_visit)

            if next_index[0] == i + 1:
                self._cells[i][j].rb = False
                self._cells[i + 1][j].lb = False
            if next_index[0] == i - 1:
                self._cells[i][j].lb = False
                self._cells[i - 1][j].rb = False
            if next_index[1] == j + 1:
                self._cells[i][j].bb = False
                self._cells[i][j + 1].tb = False
            if next_index[1] == j - 1:
                self._cells[i][j].tb = False
                self._cells[i][j - 1].bb = False

            self._break_walls_r(next_index[0], next_index[1])
