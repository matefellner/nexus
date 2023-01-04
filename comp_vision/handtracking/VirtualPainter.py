"""
Virtual painter on cam
"""

import cv2
import numpy as np
import mediapipe as mp
import HandTrackingModule as htm


###################
brushThickness = 15
eraserThickness = 30

###################


header = cv2.imread("./../images/header.png")
# print(header.shape) (63, 640, 3)

cap = cv2.VideoCapture(-1)
cap.set(3, 480)
cap.set(4, 640)
detector = htm.handDetector(detectionCon=0.85)
draw_color = (255, 255, 255)
xp, yp = 0, 0
img_canvas = np.zeros((480, 640, 3), np.uint8)


def superimpose_canvas(img, canvas):
    """
    Function to superimpose canvas on image by adding together
    """

    # True if drawn, False if empty
    canvas_mask = (canvas == 0) * 1

    # image minus canvas_mask
    image_minus_mask = np.multiply(img, canvas_mask)

    # superimposed canvas
    superimposed = np.add(image_minus_mask, canvas)

    return superimposed


while True:

    # 1. reading cam and detecting landmarks
    success, img = cap.read()
    # print(img.shape)
    img = cv2.flip(img, 1)
    img = detector.findHands(img, draw=False)
    landmarkdict = detector.findPosition(img, draw=False)

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

        # 3. selection mode
        if index_up and middle_up:
            cv2.rectangle(
                img,
                (index_x, index_y - 15),
                (middle_x, middle_y + 15),
                (255, 0, 255),
                cv2.FILLED,
            )

            # Checking for header
            if index_y < 100:
                if 0 < index_x < 124:
                    # red
                    draw_color = (1, 1, 255)
                    cv2.rectangle(
                        img,
                        (index_x, index_y - 15),
                        (middle_x, middle_y + 15),
                        draw_color,
                        cv2.FILLED,
                    )
                elif index_x < 248:
                    # green
                    draw_color = (1, 120, 1)
                    cv2.rectangle(
                        img,
                        (index_x, index_y - 15),
                        (middle_x, middle_y + 15),
                        draw_color,
                        cv2.FILLED,
                    )
                elif index_x < 372:
                    # blue
                    draw_color = (255, 1, 1)
                    cv2.rectangle(
                        img,
                        (index_x, index_y - 15),
                        (middle_x, middle_y + 15),
                        draw_color,
                        cv2.FILLED,
                    )
                elif index_x < 496:
                    # white
                    draw_color = (255, 255, 255)
                    cv2.rectangle(
                        img,
                        (index_x, index_y - 15),
                        (middle_x, middle_y + 15),
                        draw_color,
                        cv2.FILLED,
                    )
                else:
                    # erase
                    draw_color = (0, 0, 0)
                    cv2.rectangle(
                        img,
                        (index_x, index_y - 15),
                        (middle_x, middle_y + 15),
                        draw_color,
                        cv2.FILLED,
                    )

        # 4. drawing mode
        if index_up and not middle_up:
            cv2.circle(img, (index_x, index_y), 15, draw_color, cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = index_x, index_y

            if draw_color == (0, 0, 0):
                cv2.line(
                    img_canvas,
                    (xp, yp),
                    (index_x, index_y),
                    draw_color,
                    eraserThickness,
                )
            else:
                cv2.line(
                    img_canvas, (xp, yp), (index_x, index_y), draw_color, brushThickness
                )

            xp, yp = index_x, index_y
        else:
            xp, yp = 0, 0

    img[0:63, 0:640, :] = header
    # img = cv2.addWeighted(img,0.5, imgCanvas,0.5,)
    img = superimpose_canvas(img, img_canvas).astype(np.uint8)
    # print(img.shape)
    # print(img)

    cv2.imshow("Image", img)
    # cv2.imshow("Canvas", img_canvas)
    cv2.waitKey(1)
