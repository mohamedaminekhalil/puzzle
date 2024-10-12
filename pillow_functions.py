from PIL import Image
from tkinter import PhotoImage


def crop_img(path):
    """
        Crop image giving by path to 9 pieces.
    """
    im = Image.open(path)
    im = im.resize((650, 650))
    width = im.size[0]
    height = im.size[1]
    piece_height = height // 3
    piece_width = width // 3
    pieces = []
    left = 0
    upper = 0
    right = piece_width
    lower = piece_height
    piece = 0
    for _ in range(0, 3):
        for _ in range(0, 3):
            piece += 1
            box = (left, upper, right, lower)
            region = im.crop(box)
            left += piece_width
            right += piece_width
            region.save(f"images/{piece}.png")
            img = PhotoImage(file=f"images/{piece}.png")
            if piece == 9:
                break
            pieces.append(img)
        left = 0
        upper += piece_height
        right = piece_width
        lower += piece_height
    pieces.append("empty")
    return pieces
