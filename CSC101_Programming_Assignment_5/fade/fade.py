import sys
import sepia
import math
import data
import utility

# Roy Vicerra

# Task 2

# Purpose: this function takes in six inputs: 1) the current y-coordinate, 2) the current x-coordinate,
#          3) the inputted y-coordinate, 4) the inputted x-coordinate, 5) the inputted radius, and 6) the pixel value;
#          calculates and returns the data.Pixel value after a fade filter.
# Inputs: int, int, int, int, int, data.Pixel
# Output: data.Pixel

def fade_calc(curr_y: int, curr_x: int, in_y: int, in_x: int, rad: int, pixel: data.Pixel) -> data.Pixel:
    y_dist_squared = (in_y - curr_y) ** 2
    x_dist_squared = (in_x - curr_x) ** 2
    dist = math.sqrt(y_dist_squared + x_dist_squared)

    if dist >= rad:
        fade_factor = 0.2
    else:
        fade_factor = math.fabs((rad - dist) / rad)
        if fade_factor > 1:
            fade_factor = (int(fade_factor) + 1) - fade_factor
        if fade_factor < 0.2:
            fade_factor = 0.2

    red = int(pixel.red * fade_factor)
    green = int(pixel.green * fade_factor)
    blue = int(pixel.blue * fade_factor)
    con_pixel = data.Pixel(red, green, blue)

    return con_pixel


# ~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: this function takes in five inputs: 1) the image header, 2) the pixel list,
#          3) the inputted row, 4) the inputted column, and 5) the inputted radius;
#          returns the converted data.Image value with fade filter.
# Inputs: data.Header, list[data.Pixel], int, int, int
# Output: data.Image

def fade_convert(head: data.Header, pix: list[data.Pixel], y: int, x: int, rad: int) -> data.Image:
    domain = head.width
    range = head.height
    pixel_list = []
    u = 0
    v = 0
    for pixel in pix:
        if v <= (range - 1):
            if u < (domain - 1):
                con_pixel = fade_calc(v, u, y, x, rad, pixel)
                pixel_list.append(con_pixel)
                u = u + 1
            else:
                con_pixel = fade_calc(v, u, y, x, rad, pixel)
                pixel_list.append(con_pixel)
                u = 0
                v = v + 1

    processed_image = data.Image(head, pixel_list)
    return processed_image


# ~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: takes four command-line arguments: 1) image file name,
#          2) the row (y-coordinate), 3) the column (x-coordinate),
#          4) and the radius, the last three being int values;
#          converts file into faded file.
# Inputs: .ppm file, int, int, int
# Output: .ppm file

if __name__== '__main__':
    try:

        try:
            image_file = sys.argv[1]
            row = utility._convert_int(sys.argv[2], 0)
            column = utility._convert_int(sys.argv[3], 0)
            radius = utility._convert_int(sys.argv[4], 0)

        except IndexError:
            print("Please input '.ppm' file, row, column, and radius.")
            exit()

        with open(image_file) as P3_file:
            image = utility.get_image(P3_file)
            header = image.header
            pixels = image.pixels
            con_image = fade_convert(header, pixels, row, column, radius)

        with open("faded.ppm", 'w') as P3_con_file:
            con_image_str = sepia.convert_image_to_str(con_image)
            P3_con_file.write(con_image_str)

        print("Image 'faded.ppm' was successfully created.")


    except FileNotFoundError:
        print("ERROR: file does not exist. Please input a valid image file.")
        exit()