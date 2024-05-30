import win32gui
import win32ui
import win32con
import win32api

def capture_and_move_screen_part(x, y, width, height, move_x, move_y):
    # Get the device context of the entire screen
    hdc = win32gui.GetDC(0)
    # Create a device context to hold the captured part
    hdc_mem = win32ui.CreateDCFromHandle(hdc)
    mem_dc = hdc_mem.CreateCompatibleDC()
    # Create a bitmap to store the captured part
    bitmap = win32ui.CreateBitmap()
    bitmap.CreateCompatibleBitmap(hdc_mem, width, height)
    mem_dc.SelectObject(bitmap)
    # Copy the part of the screen to the memory device context
    mem_dc.BitBlt((0, 0), (width, height), hdc_mem, (x, y), win32con.SRCCOPY)
    # Paste the captured part to the new position
    hdc_mem.BitBlt((x + move_x, y + move_y), (width, height), mem_dc, (0, 0), win32con.SRCCOPY)
    # Cleanup
    win32gui.DeleteObject(bitmap.GetHandle())
    mem_dc.DeleteDC()
    hdc_mem.DeleteDC()
    win32gui.ReleaseDC(0, hdc)

# Coordonatele și dimensiunile părții de ecran pe care vrei să o muți
x, y, width, height = 100, 100, 300, 300
# Valorile de mutare pe axele x și y
move_x, move_y = 0, 50

capture_and_move_screen_part(x, y, width, height, move_x, move_y)
input()