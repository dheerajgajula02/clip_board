import clipboard
from PIL import ImageGrab, Image
import pytesseract

from plyer import notification

img = ImageGrab.grabclipboard()

img.save("saved_images/screenshort.png")


image= Image.open("saved_images/screenshort.png")

config = ('-l eng --oem 1 --psm 3')

text = pytesseract.image_to_string(image, config=config)

clipboard.copy(text)

notification.notify(
    title="Text Copied",
    message="Text copied to clipboard",
    app_icon="",
    timeout=10,

)


