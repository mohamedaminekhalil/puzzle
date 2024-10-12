import os


def remove_img(file_path):
    """
        Removing old pieces from images.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
