""""
Face mesh detection modul
"""

import cv2
import mediapipe as mp


class faceMesh:
    def __init__(self):
        """
        Constructor for face mesh detector
        """

        self.mpDraw = mp.solutions.drawing_utils
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=2)

    def findFace(self, img, draw=True):
        """
        Mediapipe face mesh detection and landmark drawing
        """

        # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = img
        self.results = self.faceMesh.process(imgRGB)

        if draw:
            if self.results.multi_face_landmarks:
                for faceLms in self.results.multi_face_landmarks:
                    self.mpDraw.draw_landmarks(
                        img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpec
                    )

        return imgRGB

    def getPosition(self, img, draw=False):
        """
        Get landmarks
        """
        landmarks = []

        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                for id, lm in enumerate(faceLms.landmark):
                    # print(lm)
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    landmarks.append((id, x, y))

        return landmarks
