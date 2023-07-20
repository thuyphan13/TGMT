import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect

video = VideoStream(src=0).start()

points = []

# new model Yolo
model = YoloDetect()

# xử lý event
def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

def draw_circles(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0,0,255), -1)
    return frame

# def draw_polygon (frame, points):
#     for point in points:
#         frame = cv2.circle( frame, (point[0], point[1]), 5, (0,0,255), -1)
#     frame = cv2.polylines(frame, [np.int32(points)], False, (0,0, 255), thickness=2)

#     return frame

detect = False
while True:
    frame = video.read()
    frame = cv2.flip(frame, 1)

    # Ve ploygon
    frame = draw_circles(frame, points)

    if detect:
        frame = model.detect(frame= frame, points= points)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        points.append(points[0])
        detect = True

    # Hien anh ra man hinh
    cv2.imshow("Room 1", frame)
    cv2.setMouseCallback('Room 1', handle_left_click, points)

video.stop()
cv2.destroyAllWindows()
