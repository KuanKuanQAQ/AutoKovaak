from PIL import ImageChops # $ pip install pillow
from pyscreenshot import grab # $ pip install pyscreenshot
import time

time.sleep(1)
im = grab()
while True: # http://effbot.org/zone/pil-comparing-images.htm
    diff = ImageChops.difference(grab(), im)
    bbox = diff.getbbox()
    if bbox is not None: # exact comparison
        break

print("bounding box of non-zero difference: %s" % (bbox,))
# superimpose the inverted image and the difference
ImageChops.screen(ImageChops.invert(im.crop(bbox)), diff.crop(bbox)).show()
input("Press Enter to exit")