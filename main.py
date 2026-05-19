from PIL import Image
import sys
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


def matrix_processing(image):
    #lookup = np.array(list('$@B%8&WM#*oahkbdpqwmZO0QLCJYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.'))
    lookup = np.array(list('@%#*+=-:.'))
    lookup = np.flip(lookup)
    total_ramps = len(lookup)

    matrix = np.array(image)
    bins = np.linspace(0,255,total_ramps, dtype=int)
    digitized = np.digitize(matrix, bins) - 1
    return lookup[digitized]

def array_to_ascii(array):
    ascii_str = ""
    for row in array:
        ascii_str = ascii_str + ''.join(row) + "\n"
    print(ascii_str)




def main():
    if len(sys.argv) == 1:
        print("Please provide the image path you want to process")
        sys.exit(1)
    else:
        image_path = sys.argv[1]

    gray_img = grayscale_resize_image(image_path, 150, 0.5)
    lookup_matrix = matrix_processing(gray_img)
    array_to_ascii(lookup_matrix)

if __name__ == "__main__":
    main()
