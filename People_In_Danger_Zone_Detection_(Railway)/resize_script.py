
from PIL import Image
import os, sys


# file:///media/yomna/New%20Volume/DEBI/uOttawa/CV/Railway/Images/3_persons_walking_in_the_corridor_5

path = "Images/3_persons_walking_in_the_corridor_5"
dirs = os.listdir( path )

# print('/')

for item in dirs:
        img_path= path+'/'+item
        if os.path.isfile(img_path):

            im = Image.open(img_path)
            #f, e = os.path.splitext(img_path)
            imResize = im.resize((40,30), Image.ANTIALIAS)
            imResize.save('Images_Resized/3_persons_walking_in_the_corridor_5_resized/' + str(item))
            print(imResize.size)