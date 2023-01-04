""""
Face detection modul
"""

import cv2
import mediapipe as mp


class faceDetector:
    def __init__(self):
        """
        Constructor for face detector
        """

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFace = mp.solutions.face_detection
        self.face = self.mpFace.FaceDetection()

    def findFace(self, img, draw=True):
        """
        Mediapipe face detection and landmark drawing
        """

        # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = img
        self.results = self.face.process(imgRGB)

        if draw:
            if self.results.detections:
                for id, detection in enumerate(self.results.detections):
                    self.mpDraw.draw_detection(imgRGB, detection)

        return imgRGB

    def getPosition(self, img, draw=False):
        """
        Get landmarks
        """

        detections = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                h, w, c = img.shape
                cx, cy = int(detection.x * w), int(detection.y * h)
                lm_list.append([id, cx, cy])
                score = detection.score
                bboxC = detection.location_data.relative_bounding_box
                bbox = (
                    int(bboxC.xmin * w),
                    int(bboxC.xmin * h),
                    int(bboxC.width * w),
                    int(bboxC.height * h),
                )

        return detections
