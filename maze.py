from graphics import Point, Cell
import random
import time


class Maze:
    def __init__(self, x0, y0, row_n, col_n, cell_size, window=None, seed=None):
        self._row_n, self._col_n = row_n, col_n
        self._cells = self._create_cells(Point(x0, y0), row_n, col_n, cell_size)
        self.window = window
        if seed:
            random.seed(seed)
        self._draw_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

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

    def _break_entrance_and_exit(self):
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

    def _reset_visited_cells(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True

        if i > 0 and not self._cells[i - 1][j].rb and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j], self.window)
            next_cell = self._solve_r(i - 1, j)
            if next_cell:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], self.window, undo=True)

        if (
            i < self._col_n - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i + 1][j].lb
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j], self.window)
            next_cell = self._solve_r(i + 1, j)
            if next_cell:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], self.window, undo=True)
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j - 1].bb:
            self._cells[i][j].draw_move(self._cells[i][j - 1], self.window)
            next_cell = self._solve_r(i, j - 1)
            if next_cell:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], self.window, undo=True)
        if (
            j < self._row_n - 1
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j + 1].tb
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1], self.window)
            next_cell = self._solve_r(i, j + 1)
            if next_cell:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], self.window, undo=True)

        return False
