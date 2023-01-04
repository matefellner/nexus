"""
Basic app for volume control with hand
"""


import cv2
import time
import numpy as np
import math
from ctypes import cast, POINTER

# only windows
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import HandTrackingModule as htm


######################

#    PARAMETERS

######################

wCam, hCam = 640, 480

######################

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0


def main():
    """
    Main function to run script
    """

    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(-1)
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.handDetector(detectionCon=0.7)

    while True:
        success, img = cap.read()

        img = detector.findHands(img)
        landmarkList = detector.findPosition(img, draw=False)

        if len(landmarkList) != 0:

            idx1, x1, y1 = landmarkList[4]
            idx2, x2, y2 = landmarkList[8]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img, (x1, y1), 15, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

            length = math.hypot(x2 - x1, y2 - y1)

            # Hand range 50 - 300
            # Volume Range -65 - 0
            vol = np.interp(length, [50, 300], [minVol, maxVol])
            volBar = np.interp(length, [50, 300], [400, 150])
            volPer = np.interp(length, [50, 300], [0, 100])
            print(int(length), vol)
            volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(
            img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2
        )

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
