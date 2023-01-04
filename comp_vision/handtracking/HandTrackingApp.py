"""
Basic hand tracking from module
"""

import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm


def main():
    """
    Main function to run script
    """

    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(-1)
    detector = htm.handDetector()

    while True:
        success, img = cap.read()

        img = detector.findHands(img)
        landmarkList = detector.findPosition(img, draw=False)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(
            img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
        )

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
