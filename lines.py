from tkinter import *
from tkinter.colorchooser import askcolor

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Рисование линий")
        self.master.geometry("400x600")

        self.color = "black"
        self.line_width = 1

        self.canvas = Canvas(self.master, bg="white", width=400, height=500)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.draw)

        self.clear_button = Button(self.master, text="Очистить", command=self.clear_canvas)
        self.clear_button.pack(side=LEFT)

        self.color_button = Button(self.master, text="Выбрать цвет", command=self.choose_color)
        self.color_button.pack(side=LEFT)

        self.width_button = Scale(self.master, from_=1, to=10, orient=HORIZONTAL, command=self.choose_width)
        self.width_button.pack(side=LEFT)

    def draw(self, event):
        x1, y1 = (event.x - self.line_width), (event.y - self.line_width)
        x2, y2 = (event.x + self.line_width), (event.y + self.line_width)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        self.color = askcolor(color=self.color)[1]

    def choose_width(self, val):
        self.line_width = int(val)

root = Tk()
paint_app = PaintApp(root)
root.mainloop()