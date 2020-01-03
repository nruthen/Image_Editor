__author__ = 'neilruthen'
from PIL import Image

def pixel_bw(img):

    w = img.size[0]
    h = img.size[1]

    new_image = Image.new("RGBA", (w, h), "white")

    blackorwhite = input("Do you want to use blackout or whiteout? ")

    color_discrimination = input("Choose a color that you want to change to black or white. ")

    if color_discrimination == "red":
        red_discrim = int(input("Choose a number from 255 to 0 to choose the intensity of red you want to black"
                            " or white out. "))
        red = True

    else:
        red = False

    if color_discrimination == "green":
        green_discrim = int(input("Choose a number from 255 to 0 to choose the intensity of green you want to black"
                            " or white out. "))
        green = True

    else:
        green = False


    if color_discrimination == "blue":
        blue_discrim = int(input("Choose a number from 255 to 0 to choose the intensity of blue you want to black"
                            " or white out. "))
        blue = True

    else:
        blue = False

    if blackorwhite == "blackout":
        for row in range(w):
            for col in range(h):
                current_pixel = img.getpixel((row, col))
                red_amt = int(current_pixel[0])
                green_amt = int(current_pixel[1])
                blue_amt = int(current_pixel[2])

                if red:                                             # checks the color of the pixel to the color that
                    if red_discrim <= red_amt:                      # person wants to white/black out and decides
                        new_image.putpixel((row, col), (0, 0, 0))   # whether to white/black it out

                    else:
                        new_image.putpixel((row, col), (red_amt, green_amt, blue_amt))

                if green:
                    if green_discrim <= green_amt:
                        new_image.putpixel((row, col), (0, 0, 0))

                    else:
                        new_image.putpixel((row, col), (red_amt, green_amt, blue_amt))

                if blue:

                    if blue_discrim <= blue_amt:
                        new_image.putpixel((row, col), (0, 0, 0))

                    else:
                        new_image.putpixel((row, col), (red_amt, green_amt, blue_amt))

    if blackorwhite == "whiteout":
        for row in range(w):
            for col in range(h):
                current_pixel = img.getpixel((row, col))
                red_amt = int(current_pixel[0])
                green_amt = int(current_pixel[1])
                blue_amt = int(current_pixel[2])

                if red:

                    if red_discrim <= red_amt:
                        new_image.putpixel((row, col), (255, 255, 255))

                    else:
                        new_image.putpixel((row, col), (red_amt, green_amt, blue_amt))

                if green:

                    if green_discrim <= green_amt:
                        new_image.putpixel((row, col), (255, 255, 255))

                    else:
                        new_image.putpixel((row, col), (red_amt, green_amt, blue_amt))

                if blue:
                    if blue_discrim <= blue_amt:
                        new_image.putpixel((row, col), (255, 255, 255))

                    else:
                        new_image.putpixel((row, col), (red_amt, green_amt, blue_amt))
    new_image.show()
