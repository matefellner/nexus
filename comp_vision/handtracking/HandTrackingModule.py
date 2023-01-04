"""
hand tracking module
"""

import cv2
import mediapipe as mp
import time


class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        """
        Constructor for hand detector class
        """

        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.detectionCon, self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        """
        Drawing hand landmarks on image
        """

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS
                    )

        return img

    def findPosition(self, img, handNo=0, draw=True):
        """
        Finding hand landmarks on image, return positions
        """

        landmarkdict = {}

        if self.results.multi_hand_landmarks:
            selectedHand = self.results.multi_hand_landmarks[handNo]

            for id, landmark in enumerate(selectedHand.landmark):
                # print(id, landmark)
                h, w, c = img.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)

                landmarkdict[id] = (cx, cy)
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return landmarkdict


def fingersUp(landmarkdict, selected):
    """
    Function to calculate whether selected finger is up

    selected = 8 for index finger
    selected = 12 for middle finger
    """

    selected_tip_x, selected_tip_y = landmarkdict[selected]
    selected_pip_x, selected_pip_y = landmarkdict[selected - 2]

    # print(selected, selected_tip_y, selected_pip_y)

    if selected_tip_y < selected_pip_y:
        return True
    else:
        return False
