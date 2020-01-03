__author__ = 'neilruthen'
__version__ = "6.7.8"

"""Can put an image through a variety of filters, find the outline of the image, and find the average color of the
image."""

from PIL import Image
import imageOpen
import edgedetection, grayscale, blackwhite, pixelbw, average
import redfilter, greenfilter, bluefilter, yellowfilter, orangefilter, purplefilter

img = imageOpen.prompt_and_set_file()
w = img.size[0]
h = img.size[1]

finished = False
while finished == False:

    choice = int(input("\n"
                       "Press 1 for your image in all the colors of the rainbow! \n "
                       "Press 2 for an outline of your image. \n "
                       "Press 3 for a gray-scale copy of your image. \n "
                       "Press 4 for a black and white copy of your image. \n "
                       "Press 5 to whiteout or blackout pixels on your image. \n "
                       "Press 6 to get the average color for your image. \n "
                       "Press 0 to exit. "))

    if choice == 0:
        finished == True
        exit()

    if choice == 1:

        redfilter.red_filter(img)
        orange_img = orangefilter.orange_filter(img)
        yellow_img = yellowfilter.yellow_filter(img)
        green_img = greenfilter.green_filter(img)
        blue_img = bluefilter.blue_filter(img)
        purple_img = purplefilter.purple_filter(img)

    if choice == 2:
        edge_img = edgedetection.edge_detection(img)

    if choice == 3:
        gray_img = grayscale.gray_scale(img)

    if choice == 4:
        blackwhite.black_white(img)

    if choice == 5:
        pixelbw.pixel_bw(img)

    if choice == 6:
        average.average_color(img)


