from win32gui import *
from win32ui import *
from win32api import *
from win32con import *
import time
def invert():
	hwnd = GetDesktopWindow()
	hdc = GetWindowDC(0)
	x = GetSystemMetrics(0)
	y = GetSystemMetrics(0)
	PatBlt(hdc, 0, 0, x, y, 5898313)
while True:
	invert()
	time.sleep(0.1)