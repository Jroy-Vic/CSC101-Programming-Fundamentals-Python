import sys
import data
import utility

# Roy Vicerra

# Task 1

# Purpose: this function takes the data.Image and converts its contents into a str value
#          so that it can be written into the .ppm file.
# Input: data.Image
# Output: str
def convert_image_to_str(img: data.Image) -> str:
    processed_image = "P3\n{} {}\n{}\n".format(img.header.width, img.header.height, img.header.max_color)

    for pixel in img.pixels:
        processed_image = processed_image + "{}\n{}\n{}\n".format(pixel.red, pixel.green, pixel.blue)

    return processed_image


# ~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: this function takes the header and pixel list of an image and converts
#          the pixel values to sepia values, restricting it to the max color value.
# Input: data.Header, list[data.Pixel]
# Output: data.Image
def sepia_convert(head: data.Header, pix: list[data.Pixel]) -> data.Image:
    ceiling = head.max_color
    pixel_list = []

    for pixel in pix:
        red = int((0.393 * pixel.red) + (0.769 * pixel.green) + (0.189 * pixel.blue))
        green = int((0.349 * pixel.red) + (0.686 * pixel.green) + (0.168 * pixel.blue))
        blue = int((0.272 * pixel.red) + (0.534 * pixel.green) + (0.131 * pixel.blue))
        if red > ceiling:
            diff = red - ceiling
            red = red - diff
        if green > ceiling:
            diff = green - ceiling
            green = green - diff
        if blue > ceiling:
            diff = blue - ceiling
            blue = blue - diff
        pixel_list.append(data.Pixel(red, green, blue))

    image_con = data.Image(head, pixel_list)
    return image_con


# ~~~~~~~~~~~~~~~~~~~~~~~~ #


# Purpose: opens .ppm file and extracts its contents, converting each pixel value into
#          sepia values using arithmetic, and creates new converted .ppm file.
# Input: .ppm file
# Output: .ppm file

if __name__ == '__main__':
    try:

        try:
            user = sys.argv[1]

        except IndexError:
            print("Please input '.ppm' file.")
            exit()

        file_path = "./images/" + user
        file_con_path = "./images/" + "sepia.ppm"
        with open(file_path) as P3_file:
            image = utility.get_image(P3_file)
            header = image.header
            pixels = image.pixels
            con_image = sepia_convert(header, pixels)

        with open(file_con_path, 'w') as P3_con_file:
            con_image_str = convert_image_to_str(con_image)
            P3_con_file.write(con_image_str)

        print("Image 'sepia.ppm' was successfully created.")

    except FileNotFoundError:
        print("ERROR: file does not exist. Please input a valid image file.")
        exit()