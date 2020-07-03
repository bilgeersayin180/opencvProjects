import cv2

#cascade_src = 'vehicle_haarcascade_dosyasi.xml'

#cascade_src = 'vehicle_haarcascade_dosyasi_2.xml'

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

rec = cv2.VideoWriter('lool.avi',fourcc,1,(640,480))

#cascade_src = 'vehicle_haarcascade_dosyasi_3.xml'

#cascade_src = 'vehicle_haarcascade_dosyasi.xml'

cascade_src = 'vehicle_haarcascade_dosyasi_2.xml'



video_src = 'Car_DataSet.avi'

#video_src = 'D:\\samsungNote5ten\\cv2_detection_dataset\\cv2_vehicle_detection_dataset\\Honda_Civic_type_R.mp4'

#video_src = 'Honda_Civic_type_R.avi'

cap = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    _,img = cap.read()

    if (type(img) == type(None)):
        break


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray,1.3)

    for(x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('Vehicle_Detection',img)
    rec.write(img)
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

    
