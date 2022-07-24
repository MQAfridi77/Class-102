import cv2

def take_snapshot():
    #initializing cv2
    #videoCaptureObject created which stats webcame (0 is the system)
    videoCaptureObject = cv2.VideoCapture(0)
    #Infinite
    result = True
    while(result):
        #Returns boolean if it is returned or not
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)
        result = False

    # releases the camera (closes camera)
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

take_snapshot()
