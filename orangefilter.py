__author__ = 'neilruthen'
from PIL import Image


def orange_filter(img):

    w = img.size[0]
    h = img.size[1]

    new_image = Image.new("RGBA", (w, h), "white")

    for row in range(w):
        for col in range(h):
            current_pixel = img.getpixel((row, col))
            red_amt = int(current_pixel[0])
            green_amt = int(current_pixel[1])
            blue_amt = int(current_pixel[2])

            average_intensity = int((red_amt + green_amt + blue_amt)/3)
            new_image.putpixel((row, col), (average_intensity, int(average_intensity/2), 0))

    new_image.show()