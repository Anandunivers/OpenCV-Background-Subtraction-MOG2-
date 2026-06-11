# Background Subtraction from then video stream and display the original and foreground masks in real-time. You can exit the video stream by pressing the 'q' key.

import cv2
import numpy as np
# read video file
org_v=cv2.VideoCapture("v3.mp4")
# mask for background subtraction
sub_m=cv2.createBackgroundSubtractorMOG2()
# # Morphology Kernel
# kernel = cv2.getStructuringElement(
#     cv2.MORPH_ELLIPSE,
#     (5, 5)
# )

# Play the video 
while True: 
    ret,frame=org_v.read() 
    # if the frame is read correctly ret is True
    if ret==True: 
        # Resize frame to fit the window
        frame = cv2.resize(frame, (640, 480))
        # apply background subtraction to the frame
        fg_mask=sub_m.apply(frame)
        # apply morphological operations to the foreground mask
        # fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)     
        # show the original frame and the foreground mask
        cv2.imshow("Original Video", frame)
        cv2.imshow("Foreground Mask", fg_mask)
        
        # Wait for 30 ms before moving on to the next frame
        if cv2.waitKey(20) & 0xff == ord('q'):
            break                               
    else:
        break
# release the video and close all windows
org_v.release()
cv2.destroyAllWindows()