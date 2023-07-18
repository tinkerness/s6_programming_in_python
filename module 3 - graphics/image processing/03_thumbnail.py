from PIL import Image

# im = Image.open("Taj_Mahal_Front.jpg")
im = Image.open("image processing\Taj_Mahal_Front.jpg")

im.thumbnail((300,300))
im.show()