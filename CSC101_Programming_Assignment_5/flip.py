import sys
import sepia
import data
import utility

# Roy Vicerra

# Task 3


# Purpose: this function takes in two inputs: 1) data.Header value and 2) a list of data.Pixel values;
#          reorganizes the list into a list of lists of data.Pixel values so that the pixels are
#          vertically-oriented; returns the list of lists.
# Input: data.Header, list[data.Pixel]
# Output: list[list[data.Pixel]]

def splitter_vertical(head: data.Header, pix: list[data.Pixel]) -> list[list[data.Pixel]]:
    domain = head.width
    total_pix = []
    sub_pix = []
    for pixel in pix:
        sub_pix.append(pixel)
        if len(sub_pix) == domain:
            total_pix.append(sub_pix)
            sub_pix = []

    return total_pix


# ~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: this function takes in two inputs: 1) data.Header value and 2) a list of data.Pixel values;
#          reorganizes the list into a list of lists of data.Pixel values so that the pixels are
#          horizontally-oriented; returns the list of lists.
# Input: data.Header, list[data.Pixel]
# Output: list[list[data.Pixel]]

def splitter_horizontal(head: data.Header, pix: list[data.Pixel]) -> list[list[data.Pixel]]:
    row = head.width
    domain = head.height
    total_pix = []
    sub_pix = []

    for idx in range(row):
        for pixel in range(domain):
            position = idx + (pixel * row)
            sub_pix.append(pix[position])
            if len(sub_pix) == domain:
                total_pix.append(sub_pix)
                sub_pix = []

    return total_pix


# ~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: this function takes in two inputs: 1) data.Header value and 2) a list of lists of data.Pixel values;
#          takes the previously vertical-oriented list of lists and reorganizes it into a single list
#          of data.Pixel values; returns a data.Image value.
# Input: data.Header, list[list[data.Pixel]]
# Output: data.Image

def process_vertical(head: data.Header, pix_split: list[list[data.Pixel]]) -> data.Image:
    pix = []

    for section in pix_split:
        for pixel in section:
            pix.append(pixel)

    processed_image = data.Image(head, pix)
    return processed_image


# ~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: this function takes in two inputs: 1) data.Header value and 2) a list of lists of data.Pixel values;
#          takes the previously horizontal-oriented list of lists and reorganizes it into a single list
#          of data.Pixel values; returns a data.Image value.
# Input: data.Header, list[list[data.Pixel]]
# Output: data.Image

def process_horizontal(head: data.Header, pix_split: list[list[data.Pixel]]) -> data.Image:
    pix = []
    domain = head.height

    for pixel in range(domain):
        for column in range(len(pix_split)):
            pix.append(pix_split[column][pixel])

    processed_image = data.Image(head, pix)
    return processed_image


# ~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: this function takes in two inputs: 1) data.Header value and 2) a list of data.Pixel values;
#          reorganizes the list and rearranges the order to apply a horizontal conversion filter;
#          processes the image and returns it as a data.Image value.
# Input: data.Header, list[data.Pixel]
# Output: data.Image

def horizontal_convert(head: data.Header, pix: list[data.Pixel]) -> data.Image:
    pix_split = splitter_horizontal(head, pix)

    for column_idx in range(len(pix_split)):
        if (head.width % 2) == 0 and column_idx < (head.width / 2):
            prev_1 = pix_split[column_idx]
            prev_2 = pix_split[(len(pix_split) - 1) - column_idx]
            pix_split[column_idx] = prev_2
            pix_split[(len(pix_split) - 1) - column_idx] = prev_1
        elif (head.width % 2) == 1 and column_idx <= (head.width / 2):
            prev_1 = pix_split[column_idx]
            prev_2 = pix_split[(len(pix_split) - 1) - column_idx]
            pix_split[column_idx] = prev_2
            pix_split[(len(pix_split) - 1) - column_idx] = prev_1

    processed_image = process_horizontal(head, pix_split)
    return processed_image


# ~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Purpose: this function takes in two inputs: 1) data.Header value and 2) a list of data.Pixel values;
#          reorganizes the list and rearranges the order to apply a vertical conversion filter;
#          processes the image and returns it as a data.Image value.
# Input: data.Header, list[data.Pixel]
# Output: data.Image

def vertical_convert(head: data.Header, pix: list[data.Pixel]) -> data.Image:
    pix_split = splitter_vertical(head, pix)

    for row_idx in range(len(pix_split)):
        if (head.height % 2) == 0 and row_idx < (head.height / 2):
            prev_1 = pix_split[row_idx]
            prev_2 = pix_split[(len(pix_split) - 1) - row_idx]
            pix_split[row_idx] = prev_2
            pix_split[(len(pix_split) - 1) - row_idx] = prev_1
        elif (head.height % 2) == 1 and row_idx <= (head.height / 2):
            prev_1 = pix_split[row_idx]
            prev_2 = pix_split[(len(pix_split) - 1) - row_idx]
            pix_split[row_idx] = prev_2
            pix_split[(len(pix_split) - 1) - row_idx] = prev_1

    processed_image = process_vertical(head, pix_split)
    return processed_image


# ~~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: opens .ppm file and extracts its contents, reorganizing its
#          order, switches the order of the pixels depending on the filter,
#          and creates two new converted .ppm files after two different filters.
# Input: .ppm file
# Output: .ppm file, .ppm file

if __name__ == '__main__':
    try:

        try:
            user = sys.argv[1]

        except IndexError:
            print("Please input '.ppm' file.")
            exit()

        file_path = "./images/" + user
        file_horizontal = "./images/" + "flip_horizontal.ppm"
        file_vertical = "./images/" + "flip_vertical.ppm"
        with open(file_path) as P3_file:
            image = utility.get_image(P3_file)
            header = image.header
            pixels = image.pixels
            image_con_horizontal = horizontal_convert(header, pixels)
            image_con_vertical = vertical_convert(header, pixels)

        with open(file_horizontal, 'w') as P3_horizontal:
            image_con_horizontal_str = sepia.convert_image_to_str(image_con_horizontal)
            P3_horizontal.write(image_con_horizontal_str)

        print("Image 'flip_horizontal.ppm' was successfully created.")

        with open(file_vertical, 'w') as P3_vertical:
            image_con_vertical_str = sepia.convert_image_to_str(image_con_vertical)
            P3_vertical.write(image_con_vertical_str)

        print("Image 'flip_vertical.ppm' was successfully created.")

    except FileNotFoundError:
        print("ERROR: file does not exist. Please input a valid image file.")
        exit()