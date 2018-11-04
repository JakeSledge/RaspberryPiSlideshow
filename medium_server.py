import shutil, os
import random
import http.server
import socketserver

PORT = 8000
PATH_TO_PICS = 'D:/Users/Jake/Desktop/Coding/Python/PhotoShuffler/PhotoLibrary'
PATH_TO_PLACE = 'D:/Users/Jake/Desktop/Coding/Python/PhotoShuffler'
PLACE = "next_pic.jpg"
os.chdir(PATH_TO_PICS)


def iterate_pic():
    if PLACE in os.listdir(PATH_TO_PLACE):
        os.chdir(PATH_TO_PLACE)
        os.remove(PLACE)
    pics = os.listdir(PATH_TO_PICS)
    rand = random.randint(0, len(pics)-1)
    next_pic_name = pics[rand]
    shutil.copy(PATH_TO_PICS + "/" + next_pic_name, PATH_TO_PLACE)
    os.chdir(PATH_TO_PLACE)
    os.rename(next_pic_name, PLACE)


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        super().do_GET()
        iterate_pic()


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port ", PORT)
    httpd.serve_forever()