from tkinter import Tk, Canvas, N, W, E, S


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

    def draw_move(self, next, window, undo=False):
        if not window:
            return
        curr_mid = Point(((self.tl.x + self.tr.x) / 2), ((self.tl.y + self.bl.y) / 2))
        next_mid = Point(((next.tl.x + next.tr.x) / 2), ((next.tl.y + next.bl.y) / 2))
        fill_color = "red"
        if undo:
            fill_color = "gray"

        Line(curr_mid, next_mid, fill=fill_color).draw(window)
