import sys
import math
import data
import ppmdiff
import utility

# Roy Vicerra

# Task 1

# Purpose: takes a float value and turns it into an int val; if
#          value is over 255, restrict it to 255.
# Input: float
# Output: int
def ceiling(val: float) -> int:
    int_val = int(val)
    if int_val > 255:
        diff = int_val - 255
        int_val = int_val - diff
    return int_val

# ~~~~~~~~~~~~~~~~~ #

# Purpose: this function takes in the str of the inputted file, converts all pixel values
#          into sepia, and returns the converted values as a str.
# Input: "P3\n3 1\n255\n0\n0\n255\n0\n255\n\n0\n0\n255"
# Output: "P3\n3 1\255\n0\n0\n125\n0\n125\n\n0\n0\n125"
def sepia_convert(file_str: str) -> str:
    file_list = file_str.splitlines()
    file_list_comp = utility._groups_of_3(file_list)
    con_file_list = []
    for pixel in range(len(file_list_comp)):                            # Writes header into sepia.ppm
        if pixel == 0:
            for value in file_list_comp[0]:
                con_file_list.append(value)
        if pixel > 0:                                                   # Writes converted pixels into sepia.ppm
            pix1 = utility._convert_int(file_list_comp[pixel][0], 0)
            pix2 = utility._convert_int(file_list_comp[pixel][1], 0)
            pix3 = utility._convert_int(file_list_comp[pixel][2], 0)
            red = (0.393 * pix1) + (0.769 * pix2) + (0.189 * pix3)
            green = (0.349 * pix1) + (0.686 * pix2) + (0.168 * pix3)
            blue = (0.272 * pix1) + (0.534 * pix2) + (0.131 * pix3)
            con_file_list.append(str(ceiling(red)))
            con_file_list.append(str(ceiling(green)))
            con_file_list.append(str(ceiling(blue)))
    con_file_str = '\n'.join(con_file_list)
    return con_file_str

# ~~~~~~~~~~~~~~~~~ #

# Purpose: opens .ppm file and extracts its contents, converting each pixel value into
#          sepia values using arithmetic, and creates new converted .ppm file.
# Input: .ppm file
# Output: .ppm file

if __name__ == '__main__':
    try:
        user = sys.argv[1]
        file_path = "./images/" + user
        file_con_path = "./images/" + "sepia.ppm"
        with open(file_path) as P3_file:
            image = P3_file.read()

        with open(file_con_path, 'w') as P3_con_file:
            image_con = sepia_convert(image)
            P3_con_file.write(image_con)

        print("Image 'sepia.ppm' created.")

    except FileNotFoundError:
        print("ERROR: file does not exist. Please input a valid image file.")
        exit()