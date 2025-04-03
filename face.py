import cv2
print(cv2.__version__)

# Provide the full path to the haarcascade_frontalface_default.xml file
face_cascade = cv2.CascadeClassifier('/full/path/to/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if TimeoutError == True:
    print("Timeout Error")

cap.release()
cv2.destroyAllWindows()

    
