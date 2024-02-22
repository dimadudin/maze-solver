class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p0, p1, fill="black") -> None:
        self.p0 = p0
        self.p1 = p1
        self.fill = fill

    def draw(self, canvas):
        canvas.create_line(
            self.p0.x, self.p0.y, self.p1.x, self.p1.y, fill=self.fill, width=4
        )


class Cell:
    def __init__(self, p0, p1) -> None:
        self.tl, self.bl = Point(p0.x, p0.y), Point(p0.x, p1.y)
        self.br, self.tr = Point(p1.x, p1.y), Point(p1.x, p0.y)
        self.lb, self.bb = True, True
        self.rb, self.tb = True, True

    def draw(self, canvas):
        colors = []
        for border in [self.lb, self.bb, self.rb, self.tb]:
            if border is True:
                colors.append("black")
            else:
                colors.append("#D9D9D9")

        Line(self.tl, self.bl, fill=colors[0]).draw(canvas)
        Line(self.bl, self.br, fill=colors[1]).draw(canvas)
        Line(self.br, self.tr, fill=colors[2]).draw(canvas)
        Line(self.tr, self.tl, fill=colors[3]).draw(canvas)
