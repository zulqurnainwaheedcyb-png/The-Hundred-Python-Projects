from PIL import Image

img = Image.open("C:\\Users\\hp\\Pictures\\nain.jpg")
img.transpose(Image.FLIP_LEFT_RIGHT).save("C:\\Users\\hp\\Pictures\\nain.jpg")