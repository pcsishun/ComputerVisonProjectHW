import numpy as np
import cv2

TARGET_SIZE = (640,360)

cap = cv2.VideoCapture(0)

thesR_B = 100
thesG_B = 0 
thesB_B = 0

thesR_L = 255
thesG_L = 50 
thesB_L = 50


while(True):
    ret,im = cap.read()
    im_resized = cv2.resize(im, TARGET_SIZE)
    im_flipped = cv2.flip(im_resized, 1)

    mask = cv2.inRange(im_flipped,(thesB_B,thesG_B,thesR_B),(thesB_L,thesG_L,thesR_L)) ## (B, G, R) ## cv2.inRange(im_flipped,(ขอบเขตเริ่มต้น น้อยสุด 0 ),(ขอบเขตมากสุด มากสุด 255)) ปรับสี เเดงตรงนี้นะ 
    

            #############################################
    h, w = im_flipped.shape[:2]
    b = im_flipped[int(h/2),int(w/2),0]
    g = im_flipped[int(h/2),int(w/2),1]
    r = im_flipped[int(h/2),int(w/2),2]

    cv2.putText(im_flipped, 'x', (int(w/2), int(h/2)),cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
    cv2.putText(im_flipped, str(b), (20, 30),cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0))
    cv2.putText(im_flipped, str(g), (90, 30),cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
    cv2.putText(im_flipped, str(r), (160, 30),cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
            #############################################
    
    print("thesR",thesR_B, "thesG",thesG_B,"thesB", thesB_B)

    if r >= 100 and b < 80 and g < 80:
        thesR_B = 100
        thesG_B = 0 
        thesB_B = 0

        thesR_L = 255
        thesG_L = 80
        thesB_L = 80

        if(np.sum(mask/255) > 0.01*h*w):
            print('Coke', r)
            cv2.putText(im_flipped,'Coke',(50,100),cv2.FONT_HERSHEY_PLAIN,8,(155,155,155)) 

    if r < 80 and b >= 100 and g < 80:
        thesR_B = 0
        thesG_B = 0 
        thesB_B = 100

        thesR_L = 80
        thesG_L = 80 
        thesB_L = 255

        if(np.sum(mask/255) > 0.01*h*w):
            print('Pepsi', b)
            cv2.putText(im_flipped,'Pepsi',(50,100),cv2.FONT_HERSHEY_PLAIN,8,(155,155,155)) 
 
 
    if r < 60 and g >= 100  and b < 60:
        thesR_B = 0
        thesG_B = 100 
        thesB_B = 0

        thesR_L = 50
        thesG_L = 255 
        thesB_L = 50

        if(np.sum(mask/255) > 0.01*h*w):
            print('7Up', g)
            cv2.putText(im_flipped,'7Up',(50,100),cv2.FONT_HERSHEY_PLAIN,8,(155,155,155)) 
    
    cv2.imshow('mask', mask)
 
 
    
    cv2.imshow('camera', im_flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()