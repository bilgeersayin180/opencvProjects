import cv2
import math
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
side_face_cascade = cv2.CascadeClassifier('MySideFace.xml')
cam = cv2.VideoCapture(0)
blue = (255, 0, 0)
red = (0,0,255)
green = (0,128,0)
w_x = 1.2
w_X = 1.2
def FaceDeetectionAverage():
    count = 0
    data_set_x = []
    data_set_y = []
    data_set_X = []
    data_set_Y = []
    while True:
        b, img = cam.read()
        #cv2.imshow("Face_recording",img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        side_faces = side_face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y),(x+w, y+h),blue, 4)
            X = x + w
            Y = y + h
            data_set_x.append(x)
            data_set_y.append(y)
            data_set_X.append(X)
            data_set_Y.append(Y)
        for (x_pos,y_pos,w_pos,h_pos) in side_faces:
            cv2.rectangle(img, (x_pos,y_pos),(x_pos + w_pos, y_pos + h_pos),green, 4)
            count += 1
        if (count >= 20):
            print("Do not turn around your face so much!")
        cv2.imshow("Face_detection",img)
        key = cv2.waitKey(1)&0xFF
        if key == ord('q'):
            break
    print(data_set_x)
    print(data_set_X)
    print(data_set_y)
    print(data_set_Y)
    def mean_cornerPoint(arr):
        product = 0
        for i in range(0, len(arr)):
            product += arr[i]
        mean = (product / len(arr))
        return mean
    def standart_deviation(array):
        Sum = 0
        MeanCornerPoint = mean_cornerPoint(array)
        for i in range(0, len(array)):
            Sum += ((array[i] - MeanCornerPoint) ** 2)
        variance = math.sqrt((Sum / (len(data_set_x) - 1)))
        return variance
    new_x = int(round(mean_cornerPoint(data_set_x)))
    new_y = int(round(mean_cornerPoint(data_set_y)))
    new_w = int(round(mean_cornerPoint(data_set_X)))
    new_h = int(round(mean_cornerPoint(data_set_Y)))
    x_variance = int(round(standart_deviation(data_set_x)))
    y_variance = int(round(standart_deviation(data_set_y)))
    X_variance = int(round(standart_deviation(data_set_X)))
    Y_variance = int(round(standart_deviation(data_set_Y)))
    print("New x: New y: New x+w: New y+h: ",new_x,new_y,new_w,new_h)
    print("Variance of x, y ,x+w , y+h : ",x_variance,y_variance,X_variance,Y_variance)
    weighted_average_variance = int(round((((x_variance * w_x) + y_variance + (X_variance * w_X) + Y_variance) / 4)))
    print("Average variance of face positions(x,y,x+w,y+h): ",weighted_average_variance)
    while True:
        b, img = cam.read()
        #cv2.imshow("Face_recording",img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y),(x+w, y+h),blue, 4)
        cv2.rectangle(img, (new_x,new_y),(new_w,new_h),red, 4)
        cv2.imshow("Face_detection",img)
        key = cv2.waitKey(1)&0xFF
        if (weighted_average_variance >= 60):
            print("Do not move your head around so much, you will lose your concentration on the traffic!")
        if key == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
FaceDeetectionAverage()

