import cv2
# import cascade file for facial recognition
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Enable camera
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
     #A picture taken from using the camera is assigned to the variable "img"

    #convert image into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Getting corners around the face
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # drawing bounding box around face
    for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h),(255, 0, 0), 2)
    cv2.imshow('img', img)
    k =cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()

