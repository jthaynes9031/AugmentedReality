import cv2

video = cv2.VideoCapture(0)


while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = video.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('g'):
        break
  
# After the loop release the cap object
video.release()
# Destroy all the windows
cv2.destroyAllWindows()


