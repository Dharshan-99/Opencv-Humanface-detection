import cv2
cap = cv2.VideoCapture(0)
while True:
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#username = input("Enter your name: ")

    

    ret,frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray, 1.0485258, 6)
    if faces is () :
         print("No faces found")
   
       


    i=0
    
    for (x,y,w,h) in faces:
        s=cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.imshow('Video', frame)
        i=i+1
         
        cv2.putText(frame, 'face num'+str(i), (x-10, y-10),cv2.LINE_4, 0.7, (0, 0, 255), 2)

          
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()