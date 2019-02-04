from PIL import Image
from pathlib import Path
import sys

image_folder = Path("../images/")
file_to_open = image_folder / sys.argv[1]
area = (600, 1200, 800, 300)
area2 = (2000, 0, 2200, 300)
im = Image.open(file_to_open)

row1 = []
for i in range(0, 2000, 500):
    row1.append(im.crop((i, 600, i+500, 1200)))
for i in row1:
    i.show()
# cropped_im1 = im.crop(area)

# cropped_im2 = im.crop(area2)
# cropped_im1.show()
