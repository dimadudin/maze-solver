from graphics import Point, Cell


class Maze:
    def __init__(self, p0, row_n, col_m, cell_size, canvas):
        self.cells = self._create_cells(p0, row_n, col_m, cell_size)
        self.canvas = canvas

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
                cell.draw(self.canvas)

    def break_cell(self, i, j):
        self.cells[i][j].tb = False
        self.cells[i][j].lb = False
        self.cells[i][j].bb = False
        self.cells[i][j].rb = False
        self.draw_cells()

    def break_st_end(self):
        self.cells[0][0].tb = False
        self.cells[-1][-1].bb = False
        self.draw_cells()
