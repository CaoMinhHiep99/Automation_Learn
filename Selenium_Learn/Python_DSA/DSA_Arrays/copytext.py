from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Controller as KeyboardController, Key
import pyautogui
import time

# Tạo đối tượng điều khiển bàn phím
keyboard = KeyboardController()

def on_click(x, y, button, pressed):
    if pressed:
        # Khi nhấn chuột, kiểm tra xem có đang bôi đen không.
        # Đây là điểm bắt đầu, giả lập thao tác copy.
        # print(f"Mouse clicked at ({x}, {y})")
        # Sử dụng Key.ctrl để mô phỏng việc nhấn Ctrl
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release(Key.ctrl)
        keyboard.release('c')
        # print("Text copied!")

def start_listener():
    with MouseListener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    start_listener()
