from tkinter import Tk, Canvas, N, W, E, S
from maze import Maze
from graphics import Point

root = Tk()
root.title("Maze Solver")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

maze = Maze(Point(100, 100), 12, 10, 100, canvas)
maze.draw_cells()
maze.break_st_end()

root.mainloop()
