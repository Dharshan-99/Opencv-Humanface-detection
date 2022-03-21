# Opencv-Humanface-detection
Detect human face using Opencv
****************
# OpenCv

OpenCV is a library of programming functions mainly aimed at real-time computer vision. What is OpenCV used for?
OpenCV is a great tool for image processing and performing computer vision tasks. It is an open-source library that can be used to perform tasks like face detection, objection tracking, landmark detection, and much more.


Import Opencv library

```
import cv2
```
To open the Camera and start capturing

```
cap = cv2.VideoCapture(0)
```
# CascadeClassifier

Haar classifiers, classifiers that were used in the first real-time face detector. A Haar classifier, or a Haar cascade classifier, is a machine learning object detection program that identifies objects in an image and video.

```
    faces = face_classifier.detectMultiScale(gray, 1.0485258, 6)
```
If face is not found by the camera...

```
if faces is () :
         print("No faces found")
```
If face is located it shows in a bounding box.

```
i=0
    
    for (x,y,w,h) in faces:
        s=cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('Video', frame)
        i=i+1
        cv2.putText(frame, 'face num'+str(i), (x-10, y-10),cv2.LINE_4, 0.7, (0, 0, 255), 2)

```
Set exit key

```

    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()

```
