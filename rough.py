import clipboard

from PIL import ImageGrab, Image

import os
from plyer import notification
import pytesseract

cmd = "xclip -selection clipboard -t image/jpeg -o > saved_images/screenshort.png"

abs_path= "/home/dheeraj/Desktop/Projects/screen_extract_script/saved_images/screenshort.png"

cmd_x = f" xclip -selection clipboard -t image/jpeg -o > {abs_path}"

os.system(cmd_x)


image = Image.open("/home/dheeraj/Desktop/Projects/screen_extract_script/saved_images/screenshort.png")

config = ('-l eng --oem 1 --psm 3')

text= pytesseract.image_to_string(image, config=config)

clipboard.copy(text)

notification.notify(
    title="Text Copied",
    message="Text copied to clipboard",
    app_icon="",
    timeout=10,
)


