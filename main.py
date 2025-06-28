import cv2
import numpy as np
import pyautogui
from ultralytics import YOLO

# Load YOLOv8 model (custom trained for hand detection)
model = YOLO("hand_detection.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Store previous hand position
prev_x = None
gesture_cooldown = 0  # To prevent multiple triggers

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    frame_height, frame_width = frame.shape[:2]

    # Assume one hand, get the first detected bounding box
    if results[0].boxes is not None and len(results[0].boxes.xyxy) > 0:
        for box in results[0].boxes.xyxy:
            x1, y1, x2, y2 = map(int, box[:4])
            cx = int((x1 + x2) / 2)

            # Draw box and center point
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.circle(frame, (cx, (y1 + y2) // 2), 5, (0, 0, 255), -1)

            if prev_x is not None and gesture_cooldown == 0:
                delta_x = cx - prev_x

                if delta_x > 60:
                    print("➡ Swipe Right Detected - Next Window")
                    pyautogui.hotkey('alt', 'tab')
                    gesture_cooldown = 20

                elif delta_x < -60:
                    print("⬅ Swipe Left Detected - Previous Window")
                    pyautogui.hotkey('alt', 'shift', 'tab')
                    gesture_cooldown = 20

            prev_x = cx
            break  # Only process one hand

    # Decrease cooldown counter
    if gesture_cooldown > 0:
        gesture_cooldown -= 1

    # Display output
    cv2.imshow("Gesture-Controlled Window Switcher", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
