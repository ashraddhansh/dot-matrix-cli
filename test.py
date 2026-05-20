from PIL import Image
import numpy as np
im = Image.open("./image.jpg")
arr = np.array(im)
ramp_size = 9

bounds = np.linspace(0, 1, ramp_size + 1)
quartiles = np.quantile(arr, bounds)[1:-1]

print(quartiles)
