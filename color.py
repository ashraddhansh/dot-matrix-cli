from PIL import Image
import numpy as np
np.set_printoptions(threshold=np.inf)


def colorize(image):
    im = Image.open(image)
    color_im = im.convert('RGB')
    matrix = np.array(color_im)
    print(matrix)

colorize("./image.jpg")
