import glob
from PIL import Image
from pathlib import Path
import os

types = ('*.jpg','*.png') # the tuple of file types
imagelist = []
for files in types:
    imagelist.extend(glob.glob(files))

im1 = Image.open(sorted(imagelist)[0])
# FIXED NoneType
im1.load()
# FIXED RGBA to RGB
if im1.mode == 'RGBA':
    im1 = im1.convert('RGB')

set_pic = []
for image in sorted(imagelist)[1:]:
    im = Image.open(image)
    # FIXED NoneType
    im.load()
    # FIXED RGBA to RGB
    if im.mode == 'RGBA':
        im = im.convert('RGB')
    set_pic.append(im)

path = Path().absolute()
folder_name = os.path.basename(path)
pdf1_filename = str(path)+'\\'+str(folder_name)+".pdf"

im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=set_pic)

