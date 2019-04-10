from PIL import Image
import os
from predict import predict
import psutil


lot_file = '/Users/mrice/Desktop/2019-03-29-05:00PM.jpg'
new_spot = '/Users/mrice/Documents/Test_Dev/Smart-Lot/image-processing-server/image-classifier-tf/tmp/tmp.png'
lot = Image.open(lot_file).rotate(1)

spot_number = 1


def kill_preview_proc():
    for proc in psutil.process_iter():
        # specific to Mac. For Linux replace 'Preview' with the 
        # name of the program that displays the image
        if proc.name() == "Preview":
            proc.kill()

# ROW 1 CROPPING 
crop_w = 200
crop_h = 250
start_x = 130
start_y = 794
stride_x = 190
row_1_spots=10
print("ROW 1 SPOTS:\n")
for i in range(row_1_spots): 
    spot = lot.crop((start_x, start_y, start_x + crop_w, start_y + crop_h))  
    start_x += stride_x 
    if i>3: start_y +=15
    spot.save(new_spot)
    prediction = predict(new_spot)
    print(f'spot {spot_number}: {prediction}')
    if prediction == 'occupied': spot.show()
    spot_number+=1
print("\n")

        
# ROW 2 CROPPING ##########################################################

crop_w = 290
crop_h = 300
start_x = 90
start_y = 1150
stride_x = 250
row_2_spots=9

print("ROW 2 SPOTS:\n")
for i in range(row_2_spots):
    spot = lot.crop((start_x, start_y , start_x + crop_w, start_y + crop_h))
    if i > 2: start_x += stride_x
    else: start_x += 270
    if i>3: start_y +=8
    spot.save(new_spot)
    prediction = predict(new_spot)
    print(f'spot {spot_number}: {prediction}')
    if prediction =='occupied': spot.show()
    spot_number+=1
print("\n")
    

# # ROW 3 CROPPING ##########################################################

crop_w = 350
crop_h = 380
start_x = 210
start_y = 1450
stride_x = 300
row_3_spots = 7

print("ROW 3 SPOTS:\n")
for i in range(row_3_spots):
    spot = lot.crop((start_x, start_y , start_x + crop_w, start_y + crop_h))
    # if i == 1: start_x += stride_x - 20
    if i > 1: start_x += stride_x
    else: start_x += 350
    if i > 1: start_y-=30
    spot.save(new_spot)
    prediction = predict(new_spot)
    print(f'spot {spot_number}: {prediction}')
    if prediction =='occupied': spot.show()
    spot_number+=1

# kill_preview_proc()