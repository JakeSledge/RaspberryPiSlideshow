import time
from PIL import Image
from http_requests import *


get_next_pic()

while True:
    get_next_pic()
    print("Got the pic")
    im = Image.open(PLACE)
    showPIL(im)
    time.sleep(30)
