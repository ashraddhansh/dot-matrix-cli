from PIL import Image
import sys
import shutil
import numpy as np
#np.set_printoptions(threshold=np.inf)


# Resize
def grayscale_resize_image(image, desired_width, correction_factor):
    im = Image.open(image)
    gray_im = im.convert('L')
    width, height = im.size[0], im.size[1]
    desired_height = int((height/width)*desired_width*correction_factor)
    resized_image = gray_im.resize((desired_width, desired_height))
    return resized_image


def matrix_processing(image, lookup, invert = False):
    total_ramps = len(lookup)

    matrix = np.array(image)
    bins = np.linspace(0,255,total_ramps, dtype=int)
    if invert:
        bins = np.flip(bins)
    digitized = np.digitize(matrix, bins) - 1
    return lookup[digitized]

def array_to_ascii(array):
    ascii_str = ""
    for row in array:
        ascii_str = ascii_str + ''.join(row) + "\n"
    print(ascii_str)




def main():
    docs = """
    Usage:
        image-to-ascii.py <image-path> [options]
    
    Options:
        --detail      Increase output detail by using a denser character ramp
        --invert      Invert character mapping (dark to light or vice versa)
        --help        For help
    
    Examples:
        image-to-ascii.py image.jpg
        image-to-ascii.py image.jpg --detail
        image-to-ascii.py image.jpg --invert
        image-to-ascii.py image.jpg --detail --invert
    """


    if len(sys.argv) == 1:
        print(docs)
        sys.exit(1)
    elif "--help" in sys.argv:
        print(docs)
    else:
        image_path = sys.argv[1]

        gray_img = grayscale_resize_image(image_path, shutil.get_terminal_size()[0], 0.5)

        detailed_ramp = np.array(list('$@B%8&WM#*oahkbdpqwmZO0QLCJYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.'))
        normal_ramp = np.array(list('@%#*+=-:.'))

        if "--detail" in sys.argv and "--invert" in sys.argv:
            lookup_matrix = matrix_processing(gray_img, detailed_ramp, invert = True)
            array_to_ascii(lookup_matrix)
        elif "--detail" in sys.argv:
            lookup_matrix = matrix_processing(gray_img, detailed_ramp)
        elif "--invert" in sys.argv:
            lookup_matrix = matrix_processing(gray_img, normal_ramp, invert= True)
        else:
            lookup_matrix = matrix_processing(gray_img, normal_ramp)
        array_to_ascii(lookup_matrix)



if __name__ == "__main__":
    main()
