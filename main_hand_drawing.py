# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:27:17 2024

@author: Rupayan Mandal
"""


'''
left hand to erase...

right hand to draw...
    1 finger --> move hand without drawing
    2 finger --> draw
    3 finger --> color change to red color
    4 finger--> coloue change to green color
    5 finger--> color change to blue color
'''



import cv2
from custom_cvzone_hand_drawing.HandTrackingModule import HandDetector
import numpy as np

cap=cv2.VideoCapture(0)

def main():
    detector=HandDetector(detectionCon=0.5,maxHands=2)
    title='Scanning'
    
    w=480
    h=640
    zero_arr=np.zeros((w,h,3),np.uint8)
    one_arr=np.ones((w,h,3),np.uint8)
    draw_radius=8
    erase_radius=80
    color=(255,255,255)
    color_name='white'
    
    while True:
        
        
        ret,img=cap.read()
        
        hands,frame=detector.findHands(img,text=title)
        
       
        if (not hands):
            title='Scanning..'
        else:
            hands1=hands[0]
            fingers=detector.fingersUp(hands1)
            count=fingers.count(1)
              #for index fingertip
            
            if (hands[0]["type"]=='Left') :
                #if (count==5):
                title="Erasing"
                cx,cy=hands[0]["center"]
                zero_arr=cv2.circle(zero_arr, (cx,cy), erase_radius, (0,0,0), thickness=-1)
                one_arr=cv2.circle(one_arr, (cx,cy), erase_radius, (1,1,1), thickness=-1)
                frame=cv2.circle(frame, (cx,cy), erase_radius, (255,255,255), thickness=-1)
                
                #else:
                 #   title="Left"
                    
                
            elif (hands[0]["type"]=='Right') :
                #tipIds = [ 8, 12, 16, 20] --> red green blue black
                if count==1:
                    color=color
                    title='move'
                
                elif count==2:
                    x,y,z=hands1['lmList'][8]
                    title="writing "+color_name
                    zero_arr=cv2.circle(zero_arr, (x,y), draw_radius, color, thickness=-1)
                    one_arr=cv2.circle(one_arr, (x,y), draw_radius, (0,0,0), thickness=-1)
                    frame=cv2.circle(frame, (x,y), draw_radius, color, thickness=-1)
                    
                elif count==3:
                    color=(0,0,255)
                    color_name='red'
                    title="color: "+color_name
                    x1,y1,z1=hands1['lmList'][12]
                    frame=cv2.circle(frame, (x1,y1), 20, color, thickness=2)
       
                    
                elif count==4:
                    color=(0,255,0)
                    color_name='green'
                    title="color: "+color_name
                    x2,y2,z2=hands1['lmList'][16]
                    frame=cv2.circle(frame, (x2,y2), 20, color, thickness=2)
       
                
                elif count==5:
                    color=(255,0,0)
                    color_name='blue'
                    title="color: "+color_name
                    x3,y3,z3=hands1['lmList'][20]
                    frame=cv2.circle(frame, (x3,y3), 20, color, thickness=2)
       
                    
                else:
                    color_name='none'
  
                
                  
        
        
        pre_final=frame*one_arr
        final=pre_final+zero_arr
        final = cv2.flip(final, 1)
        cv2.rectangle(final, (0,0),(300,100),(255, 0, 0),2)
        cv2.rectangle(final, (302,0),(350,50),color,thickness=-1)
        cv2.putText(final,title ,(50,50),  cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("Video", final)
        if ((cv2.waitKey(1)&0xFF==ord("q")) or (cv2.waitKey(1)&0xFF==ord("Q"))) :
            break
    cap.release()
    cv2.destroyAllWindows()    














if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
        cap.release()
        cv2.destroyAllWindows()
        
   
        
   












