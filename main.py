import time
import keyboard
import pyautogui as pg
import pygetwindow as gw
import win32api
import win32con


def activate_window(title):
    window = gw.getWindowsWithTitle(title)
    if window:
        window[0].activate()
        time.sleep(0.5)


window_title = "Honkai: Star Rail"

activate_window(window_title)

time.sleep(2)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def is_similar_color(color1, color2, tolerance=10):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))


target_colors = [(228, 228, 228), (255, 255, 255)]


def is_valid_color(color):
    return any(is_similar_color(color, target_color, tolerance=5) for target_color in target_colors)


while not keyboard.is_pressed('x'):
    pixel_color = pg.pixel(1142, 943)
    if is_valid_color(pixel_color):
        pg.click(1142, 943)
    else:
        print(pixel_color)
    time.sleep(2)
