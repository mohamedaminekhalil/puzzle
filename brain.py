from tkinter import PhotoImage, messagebox
from os_functions import remove_img


def moves(root, timer, canvas, event, piece_rand, pieces):
    """
        Move the selected puzzle piece up by one position.
        Updates the puzzle state accordingly.
        Call win function if pieces matches the image.
    """
    empty_pos = piece_rand.index("empty")
    if event.keysym == 'Left':
        if empty_pos not in [2, 5, 8]:
            piece_rand[empty_pos] = piece_rand[empty_pos + 1]
            piece_rand[empty_pos + 1] = "empty"
    elif event.keysym == 'Right':
        if empty_pos not in [0, 3, 6]:
            piece_rand[empty_pos] = piece_rand[empty_pos - 1]
            piece_rand[empty_pos - 1] = "empty"
    elif event.keysym == 'Up':
        if empty_pos not in [6, 7, 8]:
            piece_rand[empty_pos] = piece_rand[empty_pos + 3]
            piece_rand[empty_pos + 3] = "empty"
    elif event.keysym == 'Down':
        if empty_pos not in [0, 1, 2]:
            piece_rand[empty_pos] = piece_rand[empty_pos - 3]
            piece_rand[empty_pos - 3] = "empty"
    canvas.update_canvas(piece_rand)
    if piece_rand == pieces:
        win(root, timer, canvas, piece_rand)


def win(root, timer, canvas, piece_rand):
    """
        Stop the game and display win message.
    """
    piece_rand[8] = PhotoImage(file=f"images/{9}.png")
    canvas.update_canvas(piece_rand)
    timer.after_cancel(timer.time_)
    messagebox.showinfo(title="Won", message="You did it")
    for piece in range(0, 9):
        remove_img(f"images/{piece}.png")
    root.destroy()


def lose(root):
    """
        display losing message.
    """
    messagebox.showinfo(title="Time's up", message="You run out of time")
    for piece in range(0, 9):
        remove_img(f"images/{piece + 1}.png")
    root.destroy()
