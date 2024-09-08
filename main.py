from graphics import Window, Point, Line


def main():
    w = Window(1920, 1080)
    line = Line(Point(50, 50), Point(400, 400))
    w.draw_line(line, "black")
    w.wait_for_close()


main()
