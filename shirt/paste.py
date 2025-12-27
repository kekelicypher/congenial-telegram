from PIL import Image

img1 = Image.open("before1.jpg")
img2 = Image.open("shirt.png")

img1.paste(img2, (0, 0), img2)
img1.save("result.jpg")
