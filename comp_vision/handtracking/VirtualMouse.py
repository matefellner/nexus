"""
Virtual mouse
https://www.thepythoncode.com/article/control-mouse-python
"""

import cv2
import numpy as np
import mediapipe as mp
import mouse
import time
import pyautogui
from PIL import Image

import HandTrackingModule as htm


def main():

    ###################
    wCam, hCam = 640, 480
    screenWidth, screenHeight = pyautogui.size()
    smooth = 5
    draw_cam = False
    ###################

    pTime = 0
    last_click_time = time.time()

    prev_x, prev_y = 0, 0

    cap = cv2.VideoCapture(-1)
    cap.set(3, hCam)
    cap.set(4, wCam)
    detector = htm.handDetector(maxHands=1, trackCon=0.1)

    while True:

        # 1. reading cam and detecting landmarks
        success, img = cap.read()
        # print(img.shape)
        img = cv2.flip(img, 1)
        img = detector.findHands(img, draw=False)
        landmarkdict = detector.findPosition(img, draw=False)

        # screen = pyautogui.screenshot()
        # screen_arr = np.array(screen)
        # print(screen_arr.shape)

        # 2. detecting fingers that are up
        index_up, middle_up = False, False
        # index finger tip 8
        # middle finger tip 12
        if len(landmarkdict.keys()) > 0:
            index_up = htm.fingersUp(landmarkdict, selected=8)
            middle_up = htm.fingersUp(landmarkdict, selected=12)
            # print(index_up, middle_up)
            index_x, index_y = landmarkdict[8]
            middle_x, middle_y = landmarkdict[12]

            # 4. Moving mode
            if index_up and not middle_up:

                x = np.interp(index_x, (0, wCam), (0, screenWidth))
                y = np.interp(index_y, (0, hCam / 2), (0, screenHeight))

                # 5. Smoothen Values
                cur_x = int(prev_x + (x - prev_x) / smooth)
                cur_y = int(prev_y + (y - prev_y) / smooth)

                prev_x, prev_y = cur_x, cur_y

                if draw_cam:
                    cv2.circle(img, (index_x, index_y), 10, (255, 255, 255), cv2.FILLED)

                # 6. Move mouse
                pyautogui.moveTo(cur_x, cur_y)

            # 7. Clicking mode
            if index_up and middle_up:
                vector_index_mid_tip = np.array(landmarkdict[8]) - np.array(
                    landmarkdict[12]
                )
                finger_dist = np.linalg.norm(vector_index_mid_tip)

                if finger_dist < 40:

                    click_time = time.time()

                    if (click_time - last_click_time) > 1:

                        pyautogui.click()

                        if draw_cam:
                            cv2.circle(
                                img, (index_x, index_y), 10, (0, 255, 0), cv2.FILLED
                            )

                        last_click_time = click_time

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        print(int(fps))

        if draw_cam:
            cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
