from os import path

import cv2

samples = "/samples"
frames = "/frames"
artifacts = "/artifacts"

sample = path.join(samples, 'nbc-sports.mp4') 

vidcap = cv2.VideoCapture(sample)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(patj.join(frames, "frame%d.jpg") % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

