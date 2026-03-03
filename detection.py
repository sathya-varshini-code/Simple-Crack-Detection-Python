import cv2
import numpy as np

# Load the image
img = cv2.imread('test.jpg')

# Check if image loaded correctly
if img is None:
    print("Error: Could not find 'test.jpg'. Check your folder!")
else:
    # Process the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Show the results
    cv2.imshow('1. Original', img)
    cv2.imshow('2. Detected Cracks', edges)

    print("Success! Press any key on the image window to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()