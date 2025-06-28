# 🖐️ Gesture-Controlled Window Switcher (No MediaPipe)

Move windows without touching your mouse or keyboard — just swipe with your hand in front of the camera!

This project uses real-time computer vision with Python and OpenCV to detect left and right hand swipes, allowing you to switch between windows **hands-free**. It works by detecting the position of your hand using basic contour detection and simulating keyboard shortcuts with PyAutoGUI.

---

## 🚀 Features

- 🖥️ Real-time webcam input processing
- ✋ Simple hand detection via skin-color filtering (no mediapipe)
- ⬅️➡️ Swipe detection (left/right) to switch between windows
- 🧠 Hands-free interface for productivity or accessibility

---

## 🛠️ Tech Stack

- Python 3.13+
- OpenCV (`opencv-python`)
- NumPy
- PyAutoGUI

---

## 🧩 How It Works

1. Webcam captures live video frames.
2. The system filters skin-colored regions using HSV color space.
3. It tracks the bounding box of the hand.
4. By comparing horizontal position changes (`delta_x`) across frames, it detects swipe gestures:
   - ➡️ Right Swipe → `Alt + Tab` (next window)
   - ⬅️ Left Swipe → `Alt + Shift + Tab` (previous window)
5. PyAutoGUI simulates the keyboard shortcuts.

---

## 📦 Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/gesture-window-switcher.git
cd gesture-window-switcher
