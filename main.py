from ui import CanvasUi, TimerLabel
from tkinter import Tk, filedialog
from pillow_functions import crop_img
from brain import moves
import random

# Setup tkinter window
root = Tk()
root.withdraw()

# Window to select image
img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
root.deiconify()

# Style tkinter window
root.title("Puzzle")
root.config(width=800, height=800, background="#D4BDAB")
root.minsize(width=800, height=800)
root.maxsize(width=800, height=800)
root.resizable(False, False)
root.deiconify()

# Prepare image
pieces = crop_img(img_path)
piece_rand = pieces.copy()
random.shuffle(piece_rand)
canvas_ui = CanvasUi()
canvas_ui.update_canvas(piece_rand)
timer_ui = TimerLabel(root)

# Event listener for user input
root.bind("<KeyPress>", lambda event: moves(root, timer_ui, canvas_ui, event, piece_rand, pieces))

root.mainloop()
