from PIL import Image

def convert_to_bw(image_path):
    im = Image.open(image_path)
    # convert to black and white
    bw_image = im.convert("1")
    bw_image.show()

image_path = "module 3 - graphics\image processing\Taj_Mahal_Front.jpg"
convert_to_bw(image_path)