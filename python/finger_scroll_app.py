import cv2
import mediapipe as mp
import pyautogui

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam")
        exit()

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    previous_y = None
    previous_x = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False
        results = hands.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
                )

                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                h, w, c = frame.shape
                index_finger_cx, index_finger_cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                wrist_cx, wrist_cy = int(wrist.x * w), int(wrist.y * h)
                cv2.circle(frame, (index_finger_cx, index_finger_cy), 10, (255, 255, 255), cv2.FILLED)

                if previous_y is not None:
                    delta_y = index_finger_cy - previous_y
                    if delta_y < -20:
                        pyautogui.scroll(1)
                        print("Scrolling Up")
                    elif delta_y > 20:
                        pyautogui.scroll(-1)
                        print("Scrolling Down")
                previous_y = index_finger_cy

                if previous_x is not None:
                    delta_x = wrist_cx - previous_x
                    if delta_x < -50:
                        pyautogui.hscroll(-1)
                        print("Scrolling Left")
                    elif delta_x > 50:
                        pyautogui.hscroll(1)
                        print("Scrolling Right")
                previous_x = wrist_cx

        cv2.imshow('Finger Scroll App', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
