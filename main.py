from PIL import Image
import sys
import shutil
import numpy as np
from constants import *
#np.set_printoptions(threshold=np.inf)


# Convert image to grayscale and resizes them

def resize_image(image, desired_width, correction_factor):
    im = Image.open(image)
    width, height = im.size[0], im.size[1]
    desired_height = int((height/width)*desired_width*correction_factor)
    resized_image = im.resize((desired_width, desired_height))
    return resized_image

def color_image(image):
    color_im = image.convert('RGB')
    return color_im

def grayscale_image(image):
    gray_im = image.convert('L')
    return gray_im


# Convert image to array of brightness
# create no. of bins same as the ramps
# Interporate brightnesses from total 255 to no. of ramps
# maps those number with the ramp characters
def matrix_processing(image, lookup, invert = False, normal = False, edge_only = False, detect_edges = False):
    total_ramps = len(lookup)
    matrix = np.array(image) 
    if detect_edges:
        matrix = np.multiply(0.7,matrix) + np.multiply(0.3,edge_detector(matrix))


    if normal:
        quartile_positions = np.linspace(0, 1, total_ramps + 1)
        bins = np.quantile(matrix, quartile_positions)[1:-1]

    elif edge_only:
        bins = np.linspace(np.max(edge_detector(matrix)),np.min(matrix),total_ramps)


    else:
        bins = np.linspace(np.max(matrix),np.min(matrix),total_ramps)

    if invert:
        bins = np.flip(bins)
    
    digitized = np.digitize(matrix, bins) - 1
    return lookup[digitized]


def colorize(image, gray_matrix):
    color_matrix = np.array(image)

    line = ""
    for ascii_row, rgb_row in zip(gray_matrix, color_matrix):
        for ch, (r, g, b) in zip(ascii_row, rgb_row):
            line += f"\033[38;2;{r};{g};{b}m{ch}\033[0m"
        line += "\n"
    return line

def edge_detector(array):
    array = array.astype(float)
    height, width = array.shape
    Kx = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]])

    Ky = np.array([[1, 2, 1],
                [0, 0, 0],
                [-1, -2, -1]])
    edge_matrix = np.zeros((height, width), dtype=float)
    for row in range(1, height-1):
        for element in range(1, width-1):
            region = array[row-1:row+2, element-1:element+2]
            Gx = np.sum(region * Kx)
            Gy = np.sum(region * Ky)
            G = np.sqrt(np.square(Gx)+ np.square(Gy))
            edge_matrix[row, element] = G

    xmin = np.min(edge_matrix)
    xmax = np.max(edge_matrix)

    if xmin == xmax:
        return edge_matrix
    sub = np.subtract(edge_matrix, xmin)
    div = np.divide(sub, xmax-xmin)
    result = np.multiply(div, 255)
    return result.astype(np.uint8)


#convert array and joins characters of each row and joins the row
def array_to_ascii(gray_matrix, image=None, use_color = False):
    if use_color:
        print(colorize(image, gray_matrix))

    else:
        ascii_str = ""
        for row in gray_matrix:
            ascii_str = ascii_str + ''.join(row) + "\n"
        print(ascii_str)

def main():
    docs = """
    Usage:
        image-to-ascii.py <image-path> [options]
    
    Options:
        --detail      Increase output detail by using a denser character ramp
        --invert      Invert character mapping (dark to light or vice versa)
        --color       Colorized Output
        --help        For help
    
    Examples:
        image-to-ascii.py image.jpg
        image-to-ascii.py image.jpg --detail
        image-to-ascii.py image.jpg --invert
        image-to-ascii.py image.jpg --color
        image-to-ascii.py image.jpg --edge-only
        image-to-ascii.py image.jpg --detail --invert
        image-to-ascii.py image.jpg --detail --color
        image-to-ascii.py image.jpg --invert --color
        image-to-ascii.py image.jpg --invert --color --detail
    """

    if len(sys.argv) == 1:
        print(docs)
        sys.exit(1)
    elif "--help" in sys.argv:
        print(docs)
    else:
        image_path = sys.argv[1]


        resized_image = resize_image(image_path, shutil.get_terminal_size().columns - int(0.7*(shutil.get_terminal_size().lines)), 0.5)
        gray_img = grayscale_image(resized_image)
        color_img = color_image(resized_image)

        detail = "--detail" in sys.argv
        invert = "--invert" in sys.argv
        use_color = "--color" in sys.argv
        normal = "--normal" in sys.argv
        edge_only = "--edge-only" in sys.argv
        detect_edges = "--detect-edges" in sys.argv
        lookup = DETAILED_RAMP if detail else NORMAL_RAMP

        lookup_matrix = matrix_processing(gray_img, lookup, invert = invert, normal=normal, edge_only=edge_only, detect_edges=detect_edges)
        array_to_ascii(lookup_matrix,
                       color_img if use_color else None,
                       use_color)

if __name__ == "__main__":
    main()
