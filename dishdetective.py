# Dish detector for my kitchen 

import os
import sys
import argparse
import glob
import time

import cv2
import numpy as np
from ultralytics import YOLO

# User-defined paramters 
model_path = 'models/yolov8n.pt'
cam_source = ''
min_thresh = 
resW, resH = 640, 480
record = 

# Define box coordinates where we want to look for dishes we are going to use setup_roi.py to find this 
pbox_xmin = 
pbox_ymin = 
pbox_xmax = 
pbox_ymax = 

# set bbox colors
bbox_colors = [(164,120,87), (68,148,228), (93,97,209), (178,182,133), (88,159,106), 
              (96,202,231), (159,124,168), (169,162,241), (98,118,150), (172,176,184)]


if (not os.path.exists(model_path)):
    print('ERROR: model path is invalid/was not found.')
    sys.exit()

#load the model into memory and get labemap
model = YOLO(model_path, task='detect')
lablels = model.names

# recording settingsj
if record:
    record_name = 'demo6.avi'
    record_fps = 5
    recorder = cv2.VideoWriter(record_name, cv2.VideoWriter_fourcc(*'MJPG'), record_fps, (resW,resH))

if 'picamera' in cam_source:
    from picamera2 import Picamera2
    cam_type = 'picamera'
    cam = Picamera2()
    cam.configure(cam.create_video_configuration(main={"format": 'XRGB8888', "size": (resW, resH)}))
    cam.start()

else: 
    print('This is invalid for cam_source')
    sys.exit() 

#init fram rate variables 
avg_frame_rate = 0 
frame_rate_buffer = []
fps_avg_len = 200


while true: 
    # grab frame
    # crop this frame to the sink zone, crop numpy array using opencv
    # now give cropped image to the model, ultralytics yolo predict iamge
    #loop through results object to find all boxes
    #Filter & draw

    #motion detection ( the core of this project )
    # comparing before and after frams 
    

