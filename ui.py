from tkinter import *
from tkinter import messagebox
from os_functions import remove_img


class CanvasUi(Canvas):
    def __init__(self):
        super().__init__()
        self.configure(width=650, height=650, background="#F9DEC9", highlightbackground="#B5A192",
                       highlightthickness=4)
        self.place(x=75, y=100)

    def update_canvas(self, pieces):
        self.delete("all")
        x = 110
        y = 110
        piece = 0
        for _ in range(0, 3):
            for _ in range(0, 3):
                if piece == 9:
                    break
                elif pieces[piece] != "empty":
                    self.create_image(x, y, image=pieces[piece])
                else:
                    self.create_image(x, y)
                x += 220
                piece += 1
            y += 220
            x = 110


class TimerLabel(Label):
    def __init__(self, root):
        super().__init__()
        self.config(text="3:00", background="#D4BDAB", foreground="white",
                    font=("Helvetica", "24", "bold"))
        self.place(x=376, y=50)
        self.time = 180
        self.time_ = self.after(1000, self.timer)
        self.root = root

    def timer(self):
        self.time -= 1
        mn = self.time // 60
        sec = self.time - mn * 60
        if sec >= 10:
            self.config(text=f"0{mn}:{sec}")
        else:
            self.config(text=f"0{mn}:0{sec}")
        self.time_ = self.after(1000, self.timer)
        if self.time == 0:
            self.after_cancel(self.time_)
            messagebox.showinfo(title="Time's up", message="You run out of time")
            for piece in range(0, 9):
                remove_img(f"images/{piece + 1}.png")
            self.root.destroy()
