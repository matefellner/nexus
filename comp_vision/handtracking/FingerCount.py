"""
Basic app for finger counting
"""

import cv2
import mediapipe as mp
import time
import os
import numpy as np
import HandTrackingModule as htm


def test_finger(finger_triplet, landmarkdict, threshold=0.5):
    """
    Finger on and off detector with distance from wrist and angle of finger
    """

    tip, dip, pip = finger_triplet

    vector_1 = np.array(landmarkdict[tip]) - np.array(landmarkdict[dip])
    vector_2 = np.array(landmarkdict[dip]) - np.array(landmarkdict[pip])

    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)

    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)

    vector_tip = np.array(landmarkdict[tip]) - np.array(landmarkdict[0])
    vector_dip = np.array(landmarkdict[dip]) - np.array(landmarkdict[0])

    open_finger = np.linalg.norm(vector_dip) < np.linalg.norm(vector_tip)

    # testing for thumb
    if finger_triplet == (4, 3, 2):
        vector_tip_wrist = np.array(landmarkdict[4]) - np.array(landmarkdict[17])
        vector_wrist = np.array(landmarkdict[5]) - np.array(landmarkdict[17])
        open_finger_thumb = np.linalg.norm(vector_wrist) < np.linalg.norm(
            vector_tip_wrist
        )
        # print(np.linalg.norm(vector_wrist), np.linalg.norm(vector_tip_wrist))

        open_finger = open_finger and open_finger_thumb

    if angle < threshold and open_finger:
        return True
    else:
        return False


def main():
    """
    Main function to run script
    """

    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(-1)
    detector = htm.handDetector()

    finger_triplets = [(4, 3, 2), (8, 7, 6), (12, 11, 10), (16, 15, 14), (20, 19, 18)]

    while True:
        success, img = cap.read()

        img = detector.findHands(img, draw=False)
        landmarkdict = detector.findPosition(img, draw=False)

        if len(landmarkdict.keys()) > 0:

            count = 0

            for finger_triplet in finger_triplets:
                finger_on = test_finger(finger_triplet, landmarkdict)
                if finger_on:
                    count += 1

            cv2.putText(
                img, str(count), (10, 110), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
            )

            # cv2.circle(img, landmarkdict[4], 15, (255, 0, 255), cv2.FILLED)
            # cv2.circle(img, landmarkdict[5], 15, (0, 0, 255), cv2.FILLED)
            # cv2.circle(img, landmarkdict[17], 15, (255, 0, 0), cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        print_fps = False
        if print_fps:
            cv2.putText(
                img,
                str(int(fps)),
                (10, 70),
                cv2.FONT_HERSHEY_PLAIN,
                3,
                (255, 0, 255),
                3,
            )

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
