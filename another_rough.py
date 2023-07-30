import clipboard
from PIL import ImageGrab, Image
import pytesseract
import cv2

img = ImageGrab.grabclipboard()
img.save("saved_images/screenshort.png")

image = cv2.imread("saved_images/screenshort.png")

config = ('-l eng --oem 1 --psm 3')

print(pytesseract.image_to_string(image, config=config))