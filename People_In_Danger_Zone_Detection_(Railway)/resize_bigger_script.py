from PIL import Image
import os, sys

path = 'Images'
output_path = 'Images_Resized'

dirs = os.listdir( path )

for item in dirs:
        dir_path= path+'/'+item 

        files = os.listdir (dir_path)
        

        for filee in files:
        	img_path = path+'/'+item +'/'+filee
	        if os.path.isfile(img_path):

	            im = Image.open(img_path)
	            #f, e = os.path.splitext(img_path)
	            imResize = im.resize((40,30), Image.ANTIALIAS)
	            imResize.save('Images_Resized/'+ str(item)+'_resized/'+ str(filee))
	            print(imResize.size)
