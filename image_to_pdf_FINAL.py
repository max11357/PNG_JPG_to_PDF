import glob
from PIL import Image
from pathlib import Path
import os

# image_1st
types = ('*.jpg','*.png') # the tuple of file types
imagelist = []
for files in types:
    imagelist.extend(glob.glob(files))

im1 = Image.open(sorted(imagelist)[0]).convert('RGB')
im1.load() # FIXED NoneType

#------------------------------------------------------------------------

# set_of_image [2nd - n/a]
set_pic = []
for image in sorted(imagelist)[1:]:
    im = Image.open(image).convert('RGB')
    im.load() # FIXED NoneType

    set_pic.append(im)

path = Path().absolute()
folder_name = os.path.basename(path)
pdf1_filename = str(path)+'\\'+str(folder_name)+".pdf"

#save set_of_image to image_1st
im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=set_pic)

