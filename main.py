from PIL import Image
import sys
import numpy as np
#np.set_printoptions(threshold=np.inf)


# Resize
def grayscale_resize_image(image, desired_width):
    im = Image.open(image)
    gray_im = im.convert('L')
    width, height = im.size[0], im.size[1]
    desired_height = int((height/width)*desired_width)
    resized_image = gray_im.resize((desired_width, desired_height))
    return resized_image


def matrix_processing(image):
    lookup = np.array([".", ":", "-", "=", "+", "*", "#", "%", "@"])

    matrix = np.array(image)
    bins = [255, 240, 210, 180, 150, 120, 90, 60, 30]
    digitized = np.digitize(matrix, bins) - 1
    return lookup[digitized]




def main():
    if len(sys.argv) == 1:
        print("Please provide the image path you want to process")
        sys.exit(1)
    else:
        image_path = sys.argv[1]

    gray_img = grayscale_resize_image(image_path, 500)
    print(matrix_processing(gray_img))

if __name__ == "__main__":
    main()
