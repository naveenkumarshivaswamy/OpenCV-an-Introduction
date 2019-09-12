import cv2
import os
import time
import sys
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('Lena Söderberg.png',cv2.IMREAD_GRAYSCALE)
#
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
# plt.show()

def open_usbCam(cam=0, mirror=False, capture=False, gray=False):
    frame_counter = 0
    if isinstance(cam, int):
        usbCam = cv2.VideoCapture(cam)
    else:
        filePath = os.getcwd() + "/resource/" + str(cam)
        if os.path.exists(filePath):
            usbCam = cv2.VideoCapture(filePath)
        else:
            print("File :"+ cam + " not present in path ./resource/")
            exit(0)
    
    if (usbCam.isOpened() == False):
        print("Error opening video stream or file")
        exit(0)
        
    if capture != False:
        filename = os.getcwd() + "/resource/" + str(time.strftime("%d-%m-%Y_%H:%M:%S"))
        if capture == "video":
            # Default resolutions of the frame
            frame_width = int(usbCam.get(3))
            frame_height = int(usbCam.get(4))
            # Define the codec and create VideoWriter object
            output = cv2.VideoWriter(filename + ".avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
    
    while (usbCam.isOpened()):
        ret_val, img_frame = usbCam.read()
        
        if ret_val == True:
            frame_counter += 1
            print("frame_counter: "+str(frame_counter))
            
            if gray:
                img_frame = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
            if mirror:
                img_frame = cv2.flip(img_frame, 1)
            if capture != False and capture == "video":
                output.write(img_frame)
            
            cv2.imshow('[Press Esc/Q keys to exit/quit]', img_frame)
            
            # Press Esc/Q to exit/quit
            if (cv2.waitKey(1) == 27) or (cv2.waitKey(25) & 0xFF == ord('q')):
                if capture != False and capture == "image":
                    cv2.imwrite(filename + ".jpg", img_frame)
                break
        else:
            break
    
    # When everything done, release the video capture object
    usbCam.release()
    # output.release()
    # Closes all the frames
    cv2.destroyAllWindows()
    
def get_frameRate(standard=True):

    # Start default camera
    video = cv2.VideoCapture(0);
    
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    
    if standard:
        # With webcam get(CV_CAP_PROP_FPS) does not work.
        # Let's see for ourselves.
        if int(major_ver) < 3:
            fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
            print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
        else:
            fps = video.get(cv2.CAP_PROP_FPS)
            print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
        
        # Release video
        video.release()
        
        return fps
    else:
        # Number of frames to capture
        num_frames = 120;
        print("Capturing {0} frames".format(num_frames))
    
        # Start time
        start = time.time()
    
        # Grab a few frames
        # for i in xrange(0, num_frames):
        for i in list(range(0, num_frames)):
            ret, frame = video.read()
    
        # End time
        end = time.time()
    
        # Time elapsed
        seconds = end - start
        print("Time taken : {0} seconds".format(seconds))
    
        # Calculate frames per second
        fps = num_frames / seconds;
        print("Estimated frames per second : {0}".format(fps))
    
        # Release video
        video.release()
        
        return fps

if __name__ == '__main__':
    open_usbCam()
    # open_usbCam(cam=0)
    # open_usbCam(cam="test.mp4")
    # open_usbCam(mirror=True)
    # open_usbCam(capture="video")
    # open_usbCam(capture="image")
    # open_usbCam(gray=True)
    
    # Find OpenCV version
    # (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    # print(cv2.__version__[0])
    
    # print("FPS = ", get_frameRate())
    # print("FPS = ", get_frameRate(standard=False))

    # frameRate = 20.0
    # frameWidth = 640
    # frameHeight = 480
    #
    # cap.set(cv2.CAP_PROP_FPS, frameRate)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)