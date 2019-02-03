# code taken from https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-cv2/


# import the necessary packages
import numpy as np
import argparse
import cv2
 
#run using 'python detection.py --image ./images/Nethken_lot.png'

#construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
# ap.add_argument("-p", "--prototxt", required=False,
# 	help="path to Caffe 'deploy' prototxt file")
# ap.add_argument("-m", "--model", required=False,
# 	help="path to Caffe pre-trained model")
# ap.add_argument("-c", "--confidence", type=float, default=0.2,
# 	help="minimum probability to filter weak detections")
# args = vars(ap.parse_args())

# print(args["prototxt"])
# print(args["model"])
# print(args["confidence"])

# # initialize the list of class labels MobileNet SSD was trained to
# # detect, then generate a set of bounding box colors for each class
# CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
# 	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
# 	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
# 	"sofa", "train", "tvmonitor"]
# COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# # load our serialized model from disk
# print("[INFO] loading model...")
# net = cv2.dnn.readNetFromCaffe("./detection-models/MobileNetSSD_deploy.prototxt.txt", "./detection-models/MobileNetSSD_deploy.caffemodel")



# # load the input image and construct an input blob for the image
# # by resizing to a fixed 300x300 pixels and then normalizing it
# # (note: normalization is done via the authors of the MobileNet SSD
# # implementation)
# image = cv2.imread(args["image"])

# image = cv2.resize(image, (1200, 800))

# (h, w) = image.shape[:2]
# blob = cv2.dnn.blobFromImage(image, 0.007843,
# 	(300, 300), 127.5)

# # pass the blob through the network and obtain the detections and
# # predictions
# print("[INFO] computing object detections...")
# net.setInput(blob)
# detections = net.forward()
# print(detections.shape[2])
# # loop over the detections
# for i in np.arange(0, detections.shape[2]):
# 	# extract the confidence (i.e., probability) associated with the
# 	# prediction
# 	confidence = detections[0, 0, i, 2]
 
# 	# filter out weak detections by ensuring the `confidence` is
# 	# greater than the minimum confidence
# 	if confidence > .2:
# 		# extract the index of the class label from the `detections`,
# 		# then compute the (x, y)-coordinates of the bounding box for
# 		# the object
# 		idx = int(detections[0, 0, i, 1])
# 		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
# 		(startX, startY, endX, endY) = box.astype("int")
 
# 		# display the prediction
# 		label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
# 		print("[INFO] {}".format(label))
# 		cv2.rectangle(image, (startX, startY), (endX, endY),
# 			COLORS[idx], 2)
# 		y = startY - 15 if startY - 15 > 15 else startY + 15
# 		cv2.putText(image, label, (startX, y),
# 			cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)


# # show the output image
# cv2.imshow("Output", image)
# cv2.waitKey(0)


#run using 'python detection.py'

cascade_src = './detection-models/cars.xml'
img = cv2.imread('./images/back_of_car.png')
img = cv2.resize(img, (800, 800))
car_cascade = cv2.CascadeClassifier(cascade_src)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(img, 1.1, 1)

for (x,y,w,h) in cars:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      

cv2.imshow('image', img)
cv2.waitKey(0)

