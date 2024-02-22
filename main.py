from graphics import Window
from maze import Maze

width = 1536
height = 1536

win = Window(width, height)

row_n = 10
col_n = 10
cell_size = min(width // (row_n + 2), height // (col_n + 2))
x0, y0 = cell_size, cell_size

maze = Maze(x0, y0, row_n, col_n, cell_size, win)
maze.solve()

win.mainloop()
