import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    x1 = 250 
    y1 = 15
    x2 = 390 
    y2 = 285

    # Draw the rectangle on the original frame
    cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green color, 2px thickness

    # Convert to grayscale (if still needed)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame (use color if you want to see the rectangle clearly)
    cv.imshow('frame', frame)  # Show original frame with rectangle
    # cv.imshow('frame', gray)  # Show grayscale (comment this out if using color)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
