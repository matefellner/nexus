"""
Basic pose estimation app
"""

import cv2
import mediapipe as mp
import time
import numpy as np
import pose_estimation_module as pem

# https://google.github.io/mediapipe/solutions/pose.html#pose-landmark-model-blazepose-ghum-3d

PAIRS = [
    (11, 12),
    (12, 14),
    (14, 16),
    (16, 22),
    (16, 20),
    (16, 18),
    (18, 20),
    (12, 24),
    (11, 13),
    (13, 15),
    (15, 21),
    (15, 17),
    (15, 19),
    (17, 19),
]


def test_angles(lm_dict_1, lm_dict_2, img1, img2, draw=False):

    return img1, img2


def main():
    """
    Main function to run script
    """

    pTime = 0

    cap1 = cv2.VideoCapture("./../../data/yoga_with_adriene.mp4")
    cap2 = cv2.VideoCapture("./../../data/yoga_with_adriene.mp4")

    detector1 = pem.poseDetector()
    detector2 = pem.poseDetector()

    while True:
        success, img1 = cap1.read()
        success, img2 = cap2.read()

        print(img1.shape)

        img1 = cv2.resize(img1, (800, 450))
        img2 = cv2.resize(img2, (800, 450))

        img1 = detector1.findPose(img1)
        img2 = detector2.findPose(img2)

        landmarkdict1 = detector1.getPosition(img1, draw=False)
        landmarkdict2 = detector2.getPosition(img2, draw=False)

        img1, img2 = test_angles(lm_dict_1, lm_dict_2, img1, img2, draw=False)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        numpy_vertical_concat = np.concatenate((img1, img2), axis=0)

        cv2.putText(
            img1, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
        )

        cv2.imshow("Image", numpy_vertical_concat)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
