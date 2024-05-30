from win32gui import *
from win32ui import *
from win32api import *
from win32con import *
import time
def tunel():
    hwnd = GetDesktopWindow()
    hdc = GetWindowDC(0)
    x = GetSystemMetrics(0)
    y = GetSystemMetrics(1)
    StretchBlt(hdc, 25, 25, x - 50, y - 50, hdc, 0, 0, x, y, SRCCOPY)
while True:
	tunel()
	time.sleep(0.1)