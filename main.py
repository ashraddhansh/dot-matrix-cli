from PIL import Image
import sys

# Resize
def grayscale_resize_image(image, desired_width):
    im = Image.open(image)
    gray_im = im.convert('L')
    width, height = im.size[0], im.size[1]
    desired_height = int((height/width)*desired_width)
    resized_image = gray_im.resize((desired_width, desired_height))
    return resized_image


def main():
    if len(sys.argv) == 1:
        print("Please provide the image path you want to process")
        sys.exit(1)
    else:
        image_path = sys.argv[1]

    grayscale_resize_image(image_path, 500).save("resized_image.jpg")

if __name__ == "__main__":
    main()
