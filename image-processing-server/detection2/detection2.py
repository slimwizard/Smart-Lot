
# original source: https://github.com/ckyrkou/CNN_Car_Detector

import numpy as np
import random as rnd
import cv2
from utils import *
from make_model import *
import time
import sys

seed = 11
rnd.seed(seed)
np.random.seed(seed)

print(sys.argv[1])

############################
#### EDIT ONLY THIS BLOCK

#videofile = './test_video.mp4'
imagefile = '../image-processing-server/detection2/tmp'
frame = cv2.imread(imagefile)
#cv2.imshow("im", frame)

model = make_model()
model.load_weights('../image-processing-server/detection2/weights_best_detection2.h5')

lower = [0, 0, 0]
upper = [100, 100, 100]

stepSize = 30

############################

lower = np.array(lower)
upper = np.array(upper)



############################
#### EDIT ONLY THIS BLOCK

#Convert image to HSV from BGR
img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Find the pixels that correspond to road
img_out = cv2.inRange(img_hsv, lower, upper)

############################

# Clean from noisy pixels and keep only the largest connected segment
img_out = post_process(img_out)

image_masked = frame.copy()

# Get masked image
image_masked[img_out == 0] = (0, 0, 0)
s=0.25

#Resize images for computational efficiency
frame = cv2.resize(frame,None, fx=s,fy=s)
image_masked = cv2.resize(image_masked,None, fx=s,fy=s)

#Run the sliding window detection process
bbox_list, totalWindows, correct, score = detectionProcess(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB), model, winH=50, winW=50, depth=3, nb_images=1, scale=1, stepSize=stepSize, thres_score=0.05)

#Draw the detections
drawBoxes(frame, bbox_list)

# Draw detections and road masks
cv2.imshow('image', frame)
cv2.waitKey(0)
# time.sleep(50)
# #QUIT
# if(k & 0xFF == ord('q')):
#     cv2.destroyWindow("image")

#cv2.destroyAllWindows()
