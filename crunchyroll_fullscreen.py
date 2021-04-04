"""
Launch Web browser: http://www.crunchyroll.com

Automatically set video player to fullscreen during transition onto the next episode.
Desktop resolutions: 1080p
OS: Windows
"""

import webbrowser
import pyautogui
import time

URL = "http://www.crunchyroll.com"
CHECK_OFF_SCREEN1 = [50, 846, (242, 242, 242)]
CHECK_OFF_SCREEN2 = [249, 985, (242, 242, 242)]
FULLSCREEN_BUTTON = [1082, 590]


def check_fullscreen():
    """
    Check if web browser needs to be in fullscreen.

    If true, automatically set screen to full.

    :return: check_fullscreen - recursion
    """
    global CHECK_OFF_SCREEN1, CHECK_OFF_SCREEN2, FULLSCREEN_BUTTON

    # Unpacking variable to use to check screen position
    check_x1, check_y1, color1 = CHECK_OFF_SCREEN1
    check_x2, check_y2, color2 = CHECK_OFF_SCREEN2
    button_x, button_y = FULLSCREEN_BUTTON

    # Two position check - decrease chance of falsely detecting video player no longer in fullscreen.
    check_one = pyautogui.pixelMatchesColor(check_x1, check_y1, color1, tolerance=10)
    check_two = pyautogui.pixelMatchesColor(check_x2, check_y2, color2, tolerance=10)

    if check_one and check_two:
        pyautogui.moveTo(button_x, button_y, duration=0.2)
        time.sleep(1)
        pyautogui.click()

        return None
    else:
        time.sleep(5)
        return check_fullscreen()


def main():
    global URL

    # Launch program confirmation screen.
    start_title = "Launch Crunchyroll - Fullscreen"
    start_message = "Open Crunchyroll?\n\nAutomatically set video player to fullscreen during transition."
    pyautogui.confirm(text=start_message, title=start_title, buttons=['OK', 'Cancel'])

    # Open url
    webbrowser.open(URL, new=0, autoraise=True)

    while True:
        # Wait 20min before checking for fullscreen.
        time.sleep(1200)
        check_fullscreen()


if __name__ == "__main__":
    main()
