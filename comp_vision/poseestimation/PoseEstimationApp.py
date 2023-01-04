"""
Basic pose estimation app
"""

import cv2
import mediapipe as mp
import time
import pose_estimation_module as pem


def main():
    """
    Main function to run script
    """

    pTime = 0

    cap = cv2.VideoCapture("./../../data/yoga_with_adriene.mp4")
    detector = pem.poseDetector()

    while True:
        success, img = cap.read()

        img = detector.findPose(img)
        landmarkdict = detector.getPosition(img, draw=False)

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
