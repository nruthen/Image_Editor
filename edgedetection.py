__author__ = 'neilruthen'

from PIL import Image


def edge_detection(img):
    w = img.size[0]
    h = img.size[1]

    new_image = Image.new("RGBA", (w, h), "white")

    for row in range(w):
        for col in range(h):

            current_pixel = img.getpixel((row, col))          # changes pixel to gray scale
            red_amt = int(current_pixel[0])
            green_amt = int(current_pixel[1])
            blue_amt = int(current_pixel[2])
            gray = int(0.2989 * red_amt + 0.5870 * green_amt + 0.1140 * blue_amt)

            try:                                              # checks next pixel
                next_pixel = img.getpixel((row, col+1))       # ensures that the index error that occurs when the end
            except IndexError:                                # of the column is reached is resolved
                pass

            red_amt2 = int(next_pixel[0])
            green_amt2 = int(next_pixel[1])
            blue_amt2 = int(next_pixel[2])
            gray2 = int(0.2989 * red_amt2 + 0.5870 * green_amt2 + 0.1140 * blue_amt2)

            try:                                             # resolves index error when the end of the row is reached
                next_pixel = img.getpixel((row+1, col))
            except IndexError:
                pass

            red_amt3 = int(next_pixel[0])
            green_amt3 = int(next_pixel[1])
            blue_amt3 = int(next_pixel[2])
            gray3 = int(0.2989 * red_amt3 + 0.5870 * green_amt3 + 0.1140 * blue_amt3)

            if gray <= gray2 - 5 or gray >= gray2 + 5:     # checks for differences in the intensity of each color
                new_image.putpixel((row, col), (0, 0, 0))

            if gray <= gray3 - 5 or gray >= gray3 + 5:
                new_image.putpixel((row, col), (0, 0, 0))

    new_image.show()