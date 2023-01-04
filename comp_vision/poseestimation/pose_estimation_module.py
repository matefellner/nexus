"""
Pose estimation modul
"""

import cv2
import time
import mediapipe as mp


class poseDetector:
    def __init__(
        self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5
    ):
        """
        Constructor for pose detector
        """

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()

    def findPose(self, img, draw=True):
        """
        Mediapipe pose detection and landmark drawing
        """

        # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = img
        self.results = self.pose.process(imgRGB)

        if draw:
            if self.results.pose_landmarks:
                self.mpDraw.draw_landmarks(
                    imgRGB, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS
                )

        return imgRGB

    def getPosition(self, img, draw=False):
        """
        Get landmarks
        """

        lmdict = {}

        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmdict[id] = (cx, cy)

        return lmdict
