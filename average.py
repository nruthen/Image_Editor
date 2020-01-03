__author__ = 'neilruthen'
from PIL import Image


def average_color(img):

    w = img.size[0]
    h = img.size[1]

    red_list = []
    green_list = []
    blue_list = []
    red_intensity = 0
    green_intensity = 0
    blue_intensity = 0


    new_image = Image.new("RGBA", (w, h), "white")

    for row in range(w):
        for col in range(h):
            current_pixel = img.getpixel((row, col))
            red_amt = int(current_pixel[0])
            red_list.append(red_amt)
            red_intensity = int(red_intensity + red_amt)

            green_amt = int(current_pixel[1])
            green_list.append(green_amt)
            green_intensity = int(green_intensity + green_amt)

            blue_amt = int(current_pixel[2])
            blue_list.append(blue_amt)
            blue_intensity = int(blue_intensity + blue_amt)

            red_average = int(red_intensity/len(red_list))
            green_average = int(blue_intensity/len(blue_list))
            blue_average = int(green_intensity/len(green_list))

            new_image.putpixel((row, col), (red_average, green_average, blue_average))

    new_image.show()