from images import Image

path = input("Enter the path to the gif image: ")
factor = int(input("Enter the factor to shrink: "))

img = Image(path)
height, width = img.getHeight(), img.getWidth()
new_img = Image(width // factor, height // factor)

for newY, oldY in enumerate(range(0, height, factor)):
    for newX, oldX in enumerate(range(0, width, factor)):
        new_img.setPixel(newX, newY, img.getPixel(oldX, oldY))

new_img.draw()
