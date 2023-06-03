import cv2

# load some pretrained data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# to capture video from camera
webcam=cv2.VideoCapture(0)  # arguement 0 looks for our webcam while if we give it any name it looks for that file

# iterate over frames
while True:
    # to read current frame
    frame_read,frame = webcam.read()  # frame read is either true or flase       frame is the frame or image in the video

    # converting it to greyscale
    # greyscaled_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #  detect the face
    face_coordinates = trained_face_data.detectMultiScale(frame)   # returns top left corner coordinates and width and height if we have multiple faces we will have multiple items in the returned list with each item being a list

    # to keep a circle or rectangle around the face
    for x, y, w, h in face_coordinates:  # we are using a loop to loop over all the faces in the image
        center_x=x+w//2
        center_y=y+h//2
        radius=(w+h)//4
        circle_color=(0,255,0)
        circle_center=(center_x,center_y)
        cv2.circle(frame,circle_center,radius,circle_color,2)
        # to select the color of rectangle over face. it is (blue, green, red)
        # rectangle_color=(0,255,0)
        # cv2.rectangle(frame, (x,y), (x+w,y+h), rectangle_color,2)  # image, x,y are bottom left coordinates   x+w,y+h are bottom right coordinates    rectangle width

    # to show that image
    cv2.imshow('My Face Detector', frame)
    # to keep the image on the screen. it pauses the execution of code. it will wait until any key is pressed if time is not passed as arguement.
    # key = cv2.waitKey(1)  # time is given in 1ms
    # if we press any key it will go into the key variable. if no key is pressed it's value is -1   if any key is pressed its ascii value will be stored
    cv2.waitkey()
    # to stop if q or Q is pressed
    # if key == 81 or key == 113:
    #     break

# to release video capture object
webcam.release()


print("Code completed")