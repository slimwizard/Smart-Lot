import os, sys
from PIL import Image



# from PIL import Image

# basewidth = 200
# img = Image.open('somepic.jpg')
# wpercent = (basewidth/float(img.size[0]))
# hsize = int((float(img.size[1])*float(wpercent)))
# img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# img.save('sompic.jpg') 

size = 250, 250

for dir in os.listdir('./testing-data'):
    for infile in os.listdir(f'./testing-data/{dir}'):
        try:
            im = Image.open(f'./testing-data/{dir}/{infile}')
            new_im = im.resize(size, Image.BICUBIC)
            new_im.save(f'./testing-data/{dir}/{infile}')
        except IOError:
            print(IOError)
            print(f'cannot create thumbnail for {infile}')

for dir in os.listdir('./training-data'):
    for infile in os.listdir(f'./training-data/{dir}'):
        try:
            im = Image.open(f'./training-data/{dir}/{infile}')
            new_im = im.resize(size, Image.BICUBIC)
            new_im.save(f'./training-data/{dir}/{infile}')
        except IOError:
            print(f'cannot create thumbnail for {infile}')