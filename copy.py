# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:27:17 2024

@author: Rupayan Mandal
"""

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
    draw_radius=5
    erase_radius=50
    
    while True:
        
        
        ret,img=cap.read()
        
        hands,frame=detector.findHands(img,text=title)
        
       
        if (not hands):
            title='No data'
        else:
            hands1=hands[0]
            fingers=detector.fingersUp(hands1)
            count=fingers.count(1)
              #for index fingertip
            
            if (hands[0]["type"]=='Left') :
                if (count==5):
                    title="Erasing"
                    cx,cy=hands[0]["center"]
                    zero_arr=cv2.circle(zero_arr, (cx,cy), erase_radius, (0,0,0), thickness=-1)
                    one_arr=cv2.circle(one_arr, (cx,cy), erase_radius, (1,1,1), thickness=-1)

                    print("A")
                else:
                    title="Left"
                    
                
            elif (hands[0]["type"]=='Right') :
                
                if count==1:
                    x,y,z=hands1['lmList'][8]
                    title=hands[0]["type"]+"writing"
                    zero_arr=cv2.circle(zero_arr, (x,y), draw_radius, (0,0,255), thickness=-1)
                    one_arr=cv2.circle(one_arr, (x,y), draw_radius, (0,0,0), thickness=-1)

                else:
                    title=hands[0]["type"]+"no writing"
    
        
        
        pre_final=frame*one_arr
        final=pre_final+zero_arr
        final = cv2.flip(final, 1)
        cv2.rectangle(final, (0,0),(300,100),(255, 0, 0),2)
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
        
   
        
   
