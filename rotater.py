from PIL import Image
import os, os.path
from time import time, gmtime, strftime
path ="./"
valid_images = [".jpg"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    colorImage = Image.open(os.path.join(path,f))
    rot = colorImage.rotate(180)
    rot.save("./rotated" + strftime('%s',gmtime()) + ".jpg")





#rot.show()
