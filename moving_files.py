import shutil, os


PATH_TO_PICS = '/Users/jakesledge/Desktop/Coding/Python/PhotoStreaming/Photos'
PATH_TO_PLACE = '/Users/jakesledge/Desktop/Coding/Python/PhotoStreaming/'
os.chdir(PATH_TO_PICS)
print(os.listdir(PATH_TO_PLACE))
shutil.copy(PATH_TO_PICS + '/dog.jpg', PATH_TO_PLACE)