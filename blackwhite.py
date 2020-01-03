__author__ = 'neilruthen'
from PIL import Image


def black_white(img):

    w = img.size[0]
    h = img.size[1]

    new_image = Image.new("RGBA", (w, h), "white")

    for row in range(w):
        for col in range(h):
            current_pixel = img.getpixel((row, col))
            red_amt = int(current_pixel[0])
            green_amt = int(current_pixel[1])
            blue_amt = int(current_pixel[2])
            gray = int(0.2989 * red_amt + 0.5870 * green_amt + 0.1140 * blue_amt)

            if gray <= 128:
                new_image.putpixel((row, col), (0, 0, 0))
            else:
                new_image.putpixel((row, col), (256, 256, 256))

    new_image.show()