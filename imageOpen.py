__author__ = 'neilruthen'

from PIL import Image
from tkinter import filedialog
import tkinter as tk

def prompt_and_set_file():
    """prompt the user to open a file and return it"""
    image = None  # will store a copy of the image

    #open dialog for file/open:
    img_file = tk.filedialog.askopenfile(mode='r', filetypes=[
        ('JPEG','*.jpg'),
        ('GIF', '*.gif')
    ])

    if img_file != None:  #allows you to hit Cancel without throwing an error
        #save a copy of the image:
        image = Image.open(img_file.name).copy()

    return image
