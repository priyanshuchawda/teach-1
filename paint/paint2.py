#pip install opencv-python mediapipe numpy


import cv2
import numpy as np
import mediapipe as mp

# Initialize Mediapipe hand detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Brush settings
BRUSH_THICKNESS = 10
ERASER_THICKNESS = 50

# Colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]  # Blue, Green, Red, Black (Eraser)
color_index = 0

# Canvas
canvas = None

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame horizontally for natural interaction
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand landmarks
    result = hands.process(rgb_frame)

    # Initialize canvas if not already done
    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmarks
            landmarks = hand_landmarks.landmark

            # Get index finger tip and thumb tip coordinates
            index_finger_tip = landmarks[8]
            thumb_tip = landmarks[4]

            ix, iy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

            # Check if the thumb and index finger are close (to switch colors)
            if abs(ix - tx) < 20 and abs(iy - ty) < 20:
                color_index = (color_index + 1) % len(colors)

            # Draw or erase based on the index finger position
            cv2.circle(frame, (ix, iy), 10, colors[color_index], cv2.FILLED)

            if colors[color_index] == (0, 0, 0):  # Eraser mode
                cv2.circle(canvas, (ix, iy), ERASER_THICKNESS, colors[color_index], cv2.FILLED)
            else:
                cv2.circle(canvas, (ix, iy), BRUSH_THICKNESS, colors[color_index], cv2.FILLED)

    # Merge canvas with the frame
    blended_frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    # Show the frames
    cv2.imshow("Virtual Paint", blended_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
