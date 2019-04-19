from PIL import Image
from predict import predict

results = []
spot_number = 1
new_spot = '/tmp/tmp.png'

def extract_and_predict(lot_file):
    lot = Image.open(lot_file).rotate(-3)
    # ROW 1 CROPPING 
    crop_w = 200
    crop_h = 250
    start_x = 90
    start_y = 910
    stride_x = 190
    row_1_spots=10
    print("ROW 1 SPOTS:\n")
    for i in range(row_1_spots): 
        spot = lot.crop((start_x, start_y, start_x + crop_w, start_y + crop_h))  
        if i>3 and i<5: start_y -=20
        if i > 6: start_x += stride_x - 22
        else: start_x += stride_x 
        spot.save(new_spot)
        prediction = predict(new_spot)
        results.append({"spot": f'{spot_number}', "status": f'{prediction}'})
        print(f'spot {spot_number}: {prediction}')
        spot_number+=1

    print("\n")

            
    # ROW 2 CROPPING ##########################################################

    crop_w = 290
    crop_h = 300
    start_x = 60
    start_y = 1200
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
        results.append({"spot": f'{spot_number}', "status": f'{prediction}'})
        print(f'spot {spot_number}: {prediction}')
        spot_number+=1
    print("\n")
        

    # # ROW 3 CROPPING ##########################################################

    crop_w = 350
    crop_h = 400
    start_x = 210
    start_y = 1500
    stride_x = 280
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
        results.append({"spot": f'{spot_number}', "status": f'{prediction}'})
        print(f'spot {spot_number}: {prediction}')
        spot_number+=1

    return results

    # kill_preview_proc()