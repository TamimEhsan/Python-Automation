import pyautogui
import win32gui

def get_pixel_colour(i_x, i_y):
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)
 
dinoposX, dinoposY = pyautogui.position()
dino = get_pixel_colour(dinoposX, dinoposY)
dinoposX = dinoposX + 23
while True :
    flag = 0
    obs = get_pixel_colour(210, 250)
    obs2 = get_pixel_colour(190, 250)
    obs3 = get_pixel_colour(220, 250)
    obs4 = get_pixel_colour(230, 250)
    if dino == obs or dino == obs2 or dino == obs3 or dino == obs4 :
        pyautogui.press('space')
    



