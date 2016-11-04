"""
Lightweight Graphics Library abstraction over tkinter/PIL

This simple library only serves to provide access to PIL image
processing functionality through simple function syntax, rather
than a mix of functions, methods and modules.
"""

import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageOps, ImageChops

def open_window(width, height):
    """
    Opens a new GUI window with the specified width and height.
    """
    global tk
    global root
    global canvas
    global tkimgs
    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()
    tkimgs = []

def update():
    """
    Updates the open graphics window so any changes that have been
    made are seen.
    """
    root.update()

def create_image(width, height):
    """
    Creates and returns a new RGB image object with the specified width
    and height. All pixels are initially set to (0,0,0).
    """
    return Image.new("RGB", (width, height))

def load_image(filename):
    """
    Reads the specified image file from disk and returns it as
    a PIL Image object.
    """
    img = Image.open(filename)
    return img

def show_image(image, x, y):
    """
    Displays the given image in the GUI window at the specified position.
    The position is x,y coordinates within the GUI window where the center
    of the image will be placed. 0,0 is the top left corner.
    """
    tkimg = ImageTk.PhotoImage(image)
    canvas.create_image(x, y, image=tkimg)
    tkimgs.append(tkimg)

def resize_image(image, width, height):
    """
    Returns a copy of the given image resized to width, height.
    """
    return image.resize((width,height))

def rotate_image(image, degrees):
    """
    Returns a copy of the given image rotated clockwise by the
    specified degrees.
    """
    return image.rotate(degrees)

def invert_image(image):
    """
    Returns a copy of the given image with each pixel value inverted.
    """
    return ImageOps.invert(image)

def grayscale_image(image):
    """
    Returns a copy of the given image with each pixel converted to
    grayscale.
    """
    return ImageOps.grayscale(image)

def flip_image(image):
    """
    Returns a copy of the given image flipped vertically.
    """
    return ImageOps.flip(image)
 
def mirror_image(image):
    """
    Returns a copy of the given image flipped horizontally.
    """
    return ImageOps.mirror(image)
 
def blend_images(img1, img2, alpha):
    """
    Returns a new image made by combining the two images.
     Each pixel position is added together to get the new image.
     The two images *must* be the same size (see resize_image).
     The two images *must* both be colored or grayscale.
    The alpha parameter (0.0 to 1.0) is the weight given to the
    values from the second image.
    """
    return ImageChops.blend(img1, img2, alpha)

def get_pixels(im):
    """
    Returns an object that provides read and write access to the
    specified image's pixel data.
    """
    return Pixels(im.load())

class Pixels:
    """
    Abstracts over the PIL PixelAccess class to provide a more beginner-
    friendly way to read and write pixel data.
    """

    def __init__(self, pa):
        self.pa = pa

    def getpixel(self, i, j):
        return self.pa[i,j]

    def setpixel(self, i, j, color):
        self.pa[i,j] = color
    
