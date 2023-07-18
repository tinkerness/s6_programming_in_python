from PIL import Image

im = Image.open("image processing\Taj_Mahal_Front.jpg").convert('L')
im.show()