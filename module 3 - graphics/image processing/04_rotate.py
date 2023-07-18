from PIL import Image

im = Image.open("image processing\Taj_Mahal_Front.jpg")
im.rotate(45).show()