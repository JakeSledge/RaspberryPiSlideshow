# Running in python 2.7.15

import urllib
import os

URL = "http://192.168.0.110:8000/next_pic.jpg"
PLACE = "pic.jpg"

def get_next_pic():
    resource = urllib.urlopen(URL)
    output = open(PLACE,"wb")
    output.write(resource.read())
    output.close()

def delete_last_pic():
    os.remove(PLACE)

get_next_pic()