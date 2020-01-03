__author__ = 'neilruthen'
from PIL import Image
import colorsys


new_image = Image.new("RGBA", (w, h), "white")

for row in range(w):
        for col in range(h):
            current_pixel = img.getpixel((row, col))
            red_amt = int(current_pixel[0])
            green_amt = int(current_pixel[1])
            blue_amt = int(current_pixel[2])
            HSV = colorsys.rgb_to_hsv(red_amt, green_amt, blue_amt)
            new_image.putpixel((col, row), HSV)
new_image.show()