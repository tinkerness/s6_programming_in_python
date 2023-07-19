'''To shrink an image by a given factor, use the resize() method and provide the new dimensions based on the original image's size and the given factor. If the factor is less than 1, the resulting image will be smaller.'''

from PIL import Image

def shrink_image_by_factor(image_path, factor):
    im = Image.open(image_path)
    original_width, original_height = im.size

    new_width = int(original_width * factor)
    new_height = int(original_height * factor)
    # Resize the image
    shrunken_image = im.resize((new_width, new_height))
    shrunken_image.show()

image_path = "module 3 - graphics\image processing\Taj_Mahal_Front.jpg"
shrink_factor = 0.25
shrink_image_by_factor(image_path, shrink_factor)