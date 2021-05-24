from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{timestamp}.mov'
fourcc = cv2.VideoWriter_fourcc('m', 'o', 'v', 'v')
captured_video = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorder-Python', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break