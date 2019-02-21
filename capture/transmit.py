from time import sleep
from datetime import datetime
import picamera
import requests
from os import remove

# initialize the camer
camera = picamera.PiCamera()

# url for local instance of API
API = 'http://127.0.0.1:5000/smart-lot/lots/upload'
#API = 'http://ec2-3-81-138-55.compute-1.amazonaws.com/smart-lot/lots/upload'

# runs every 15 seconds
while True:
    # get hour of day (military time)
    current_hour = datetime.now().hour
    # check if current time is between 9 am (hour = 9) and 5 pm (hour = 17)
    if current_hour >= 9 and current_hour <= 17:
        # capture image
        camera.capture('file.jpg')
        # send POST request to API endpoint
        files = {'file': open('file.jpg', 'rb')}
        requests.post(API, files=files)
        # delete file
        remove('file.jpg')
    sleep(15)
