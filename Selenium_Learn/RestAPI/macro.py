from pynput.mouse import Listener
from pynput.keyboard import Controller, Key
import time

# Khởi tạo đối tượng keyboard controller để gửi phím
keyboard = Controller()

# Biến lưu thời gian giữa các lần click
last_click_time = 0
double_click_time_limit = 0.3  # Giới hạn thời gian giữa các click (0.3s)

def on_click(x, y, button, pressed):
    global last_click_time
    
    if pressed:
        current_time = time.time()
        # Kiểm tra nếu là double-click
        if current_time - last_click_time <= double_click_time_limit:
            # Gửi Ctrl + C nếu là double-click
            time.sleep(0.1)
            keyboard.press(Key.ctrl_l)  # Dùng Key.ctrl_l cho phím Ctrl
            keyboard.press('c')         # Gửi phím C
            time.sleep(0.1)
            keyboard.release('c')       # Thả phím C
            keyboard.release(Key.ctrl_l)  # Thả phím Ctrl
            print("Ctrl + C được gửi.")
        last_click_time = current_time

# Lắng nghe sự kiện chuột
with Listener(on_click=on_click) as listener:
    listener.join()
