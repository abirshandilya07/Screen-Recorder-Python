# Screen-Recorder-Python
Made a screen recorder in python in less than 25 lines of code
---
For using this recorder you have to install python (obviously) and the following libraries:
1. opencv-contrib-python
2. numpy
3. pywin32
4. pillow
---
After you are done with the setup you have to import the libraries..
```
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime
```
Now that you have imported the libraries you have to declare some variables
```
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{timestamp}.mov'
fourcc = cv2.VideoWriter_fourcc('m', 'o', 'v', 'v')
captured_video = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))
```
And the actual recording part comes here..
```
while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorder-Python', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
```
In this we do the recording and save a mov file in the same folder in which your program is there

I hope you like that..
