
import cv2

# Provide the full path to the image file
img = cv2.imread('c:/Users/r58fa/OneDrive/Desktop/priyanshuchawda/teach/image/image.jpg')
if img is None:
    print("Error: Could not open or find the image.")
else:
    blurred = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imshow('Blurred Image', blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()