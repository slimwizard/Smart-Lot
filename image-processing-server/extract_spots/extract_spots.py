from PIL import Image
import os
import psutil
import sys,tty
import subprocess

image_path = '../lot_images_1'
save_to_path = '../spot_images'
# test_image_path = '/Users/mrice/Workspace/smart_lot_data/test_lot_images'

occupied_spots = 0
unoccupied_spots = 0

tty.setcbreak(sys.stdin) 

def kill_preview_proc():
    for proc in psutil.process_iter():
        # specific to Mac. For Linux replace 'Preview' with the 
        # name of the program that displays the image
        if proc.name() == "Preview":
            proc.kill()

def save_image(isOccupied, spot):
    if isOccupied: spot.save(f'{save_to_path}/occupied_spots/occupied_{occupied_spots}.png')
    else: spot.save(f'{save_to_path}/unoccupied_spots/unoccupied_{unoccupied_spots}.png')
        
def extract(spot):
    global occupied_spots
    global unoccupied_spots
    spot.show()
    subprocess.call('code')
    while True:
        key = ord(sys.stdin.read(1))
        if key:
            # 'v' key; occupied spot
            if key==118:
                save_image(True, spot)
                occupied_spots+=1
            # any other key; empty spot
            elif key!=99:    
                save_image(False, spot)
                unoccupied_spots+=1
            kill_preview_proc()
            break

for filename in os.listdir(image_path):
    # ignore .DS_Store file used by MacOS
    if filename == '.DS_Store': continue
    lot = Image.open(f'{image_path}/{filename}').rotate(1)

    # ROW 1 CROPPING 
    crop_w = 200
    crop_h = 250
    start_x = 130
    start_y = 794
    stride_x = 190
    row_1_spots=10

    for i in range(row_1_spots): 
        spot = lot.crop((start_x, \ 
        start_y,            \
        start_x + crop_w,   \ 
        start_y + crop_h))  \
        start_x += stride_x \
        if i>3: start_y +=8 \
        extract(spot)
            
    # ROW 2 CROPPING ##########################################################

    crop_w = 290
    crop_h = 300
    start_x = 90
    start_y = 1150
    stride_x = 250
    row_2_spots=9

    for i in range(row_2_spots):
        spot = lot.crop((start_x, start_y , start_x + crop_w, start_y + crop_h))
        if i > 2: start_x += stride_x
        else: start_x += 270
        if i>3: start_y +=8
        extract(spot)

    # ROW 3 CROPPING ##########################################################

    crop_w = 350
    crop_h = 380
    start_x = 210
    start_y = 1450
    stride_x = 300
    row_3_spots = 7

    for i in range(row_3_spots):
        spot = lot.crop((start_x, start_y , start_x + crop_w, start_y + crop_h))
        if i > 1: start_x += stride_x
        else: start_x += 350
        extract(spot)

