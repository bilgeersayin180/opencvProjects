import cv2
videoSource = 'Car_DataSet.avi'
cascade_src = 'vehicle_haarcascade_dosyasi_2.xml'
cap= cv2.VideoCapture(videoSource)
jpgNum = 1
red = (0,0,255)
carPlateCascade = cv2.CascadeClassifier(cascade_src)
while(True):
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    carPlate = carPlateCascade.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in carPlate:
        cv2.rectangle(img, (x,y),(x+w, y+h),red, 4)
        height = y + h
        width = x + w
        imgCropped = img[y:height,x:width]
        cv2.imwrite('plate'+str(jpgNum)+'.jpg',imgCropped)
        jpgNum+=1
    cv2.imshow("Face_detection",img)
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
