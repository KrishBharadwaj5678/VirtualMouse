import cv2
from cvzone.HandTrackingModule import HandDetector
import mouse
import numpy as np
import threading
import time

cap = cv2.VideoCapture(0)
cam_w, cam_h = 640, 480
cap.set(3,cam_w)
cap.set(4,cam_h)
detector = HandDetector(detectionCon=0.9,maxHands=1)

frameR = 100

l_delay = 0   # Left click cooldown flag
r_delay = 0   # Right click cooldown flag
d_delay = 0   # Double click cooldown flag

def l_clk_delay():
    global l_delay
    global l_clk_thread
    time.sleep(1) # Wait 1 second
    l_delay = 0   # Re-enable left click
    l_clk_thread = threading.Thread(target=l_clk_delay)  # Reset the thread

def r_clk_delay():
    global r_delay
    global r_clk_thread
    time.sleep(1) # Wait 1 second
    r_delay = 0  # Re-enable right click
    r_clk_thread = threading.Thread(target=r_clk_delay)  # Reset the thread

def d_clk_delay():
    global d_delay
    global d_clk_thread
    time.sleep(1) # Wait 1 second
    d_delay = 0  # Re-enable double click
    d_clk_thread = threading.Thread(target=d_clk_delay)  # Reset the thread

l_clk_thread = threading.Thread(target=l_clk_delay)
r_clk_thread = threading.Thread(target=r_clk_delay)
d_clk_thread = threading.Thread(target=d_clk_delay)

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img, flipType=False)
    cv2.rectangle(img,(frameR, frameR), (cam_w - frameR, cam_h - frameR),(255,0,255),2)

    if hands:
        lmList = hands[0]['lmList']
        ind_x, ind_y = lmList[8][0], lmList[8][1] # Index fingertip
        mid_x, mid_y = lmList[12][0], lmList[12][1] # Middle fingertip
        cv2.circle(img,(ind_x,ind_y),5,(0,255,255),2)
        fingers = detector.fingersUp(hands[0]) # List of finger states

        # Mouse Movement
        if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 1:
            conv_x = int(np.interp(ind_x,(frameR,cam_w - frameR),(0,1920)))
            conv_y = int(np.interp(ind_y,(frameR,cam_h - frameR),(0,1080)))
            mouse.move(conv_x,conv_y)

        #Left Click
        if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 1:
            if abs(ind_x - mid_x) < 25:
                if fingers[4] == 0 and l_delay == 0:
                    mouse.click(button="left")  # Trigger click
                    l_delay = 1  # Set cooldown flag
                    l_clk_thread.start()  # Start delay countdown

                # Right Click
                if fingers[4] == 1 and r_delay == 0:
                    mouse.click(button="right")  # Trigger click
                    r_delay = 1  # Set cooldown flag
                    r_clk_thread.start()  # Start delay countdown

        # Scroll Down
        if fingers[1] == 1 and fingers[2] == 1 and fingers[4] == 0 and fingers[0] == 0:
            if abs(ind_x - mid_x) < 25:
                mouse.wheel(delta=-1)

        # Scroll Up
        if fingers[1] == 1 and fingers[2] == 1 and fingers[4] == 1 and fingers[0] == 0:
            if abs(ind_x - mid_x) < 25:
                mouse.wheel(delta=1)

        # Double click
        if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 0 and fingers[4] == 0 and d_delay == 0:
            d_delay = 1  # Set cooldown flag
            mouse.double_click(button="left")  # Trigger click
            d_clk_thread.start()  # Start delay countdown

    cv2.imshow("Camera Feed",img)
    cv2.waitKey(1)