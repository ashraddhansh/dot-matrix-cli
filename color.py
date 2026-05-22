from PIL import Image
import numpy as np
np.set_printoptions(threshold=np.inf)


im = Image.open("./image.jpg")
color_im = im.convert('L')
resize_im = color_im.resize((500,800))
matrix = np.array(resize_im)


def edge_detector(array):
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
    return edge_matrix

edge_detector(matrix)
