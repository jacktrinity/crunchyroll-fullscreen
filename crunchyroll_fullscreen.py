"""
Launch Web browser: http://www.crunchyroll.com

Automatically set video player to fullscreen during transition onto the next episode.
Desktop resolutions: 1080p
OS: Windows

Written in Python 3
"""

import webbrowser
import pyautogui
import time

URL = "http://www.crunchyroll.com"
CHECK_OFF_SCREEN1 = [50, 846, (242, 242, 242)]
CHECK_OFF_SCREEN2 = [249, 985, (242, 242, 242)]
CHECK_OFF_SCREEN3 = [411, 326, (242, 242, 242)]
CHECK_OFF_SCREEN4 = [1541, 333, (242, 242, 242)]
HIGHLIGHT_SCREEN_BUTTON = [1067, 578, (242, 242, 242)]
FULLSCREEN_BUTTON = [1082, 590]


def check_fullscreen():
    """
    Check if web browser needs to be in fullscreen.

    If true, automatically set screen to full.

    :return: check_fullscreen - recursion
    """
    global CHECK_OFF_SCREEN1, CHECK_OFF_SCREEN2, CHECK_OFF_SCREEN3, CHECK_OFF_SCREEN4
    global HIGHLIGHT_SCREEN_BUTTON, FULLSCREEN_BUTTON
    
    def check_screen():
        """
        Check 4 different point on the screen to see whether or not the screen needs to be fullscreen again.
        Check to see if the fullscreen button is available.

        :return:True or False
        """
        # Unpacking variable to use to check screen position
        check_x1, check_y1, color1 = CHECK_OFF_SCREEN1
        check_x2, check_y2, color2 = CHECK_OFF_SCREEN2
        check_x3, check_y3, color3 = CHECK_OFF_SCREEN3
        check_x4, check_y4, color4 = CHECK_OFF_SCREEN4

        # Four position check - decrease chance of falsely detecting video player no longer in fullscreen.
        check_one = pyautogui.pixelMatchesColor(check_x1, check_y1, color1, tolerance=10)
        check_two = pyautogui.pixelMatchesColor(check_x2, check_y2, color2, tolerance=10)
        check_three = pyautogui.pixelMatchesColor(check_x3, check_y3, color3, tolerance=10)
        check_four = pyautogui.pixelMatchesColor(check_x4, check_y4, color4, tolerance=10)
        
        if check_one and check_two and check_three and check_four:
            return True
        else:
            return False

    # Unpacking variable to use to check fullscreen button.
    highlight_x, highlight_y, white = HIGHLIGHT_SCREEN_BUTTON
    button_x, button_y = FULLSCREEN_BUTTON
    
    if check_screen():
        # Needs to wait for the video to load before attempting to fullscreen.
        time.sleep(30)

        # Move the cursor into position.
        pyautogui.moveTo(button_x, button_y, duration=0.2)
        time.sleep(1)

        # Check to see if the fullscreen button is highlighted.
        # Highlight button is a black shade. Return False if white is detected.
        print("Button check")
        button_check = pyautogui.pixelMatchesColor(highlight_x, highlight_y, white, tolerance=10)

        if not button_check:
            print("Clicking fullscreen buttton.")
            pyautogui.click()
            return None

    # If fullscreen is not ready, return check_fullscreen().
    time.sleep(5)
    return check_fullscreen()


def main():
    global URL

    # Launch program confirmation screen.
    start_title = "Launch Crunchyroll - Fullscreen"
    start_message = "Open Crunchyroll?\n\nAutomatically set video player to fullscreen during transition."
    pyautogui.confirm(text=start_message, title=start_title, buttons=['OK', 'Cancel'])
    print("Starting Crunchyroll fullscreen detection.")

    # Open url
    webbrowser.open(URL, new=0, autoraise=True)

    while True:
        # Wait 20min before checking for fullscreen.
        print("Waiting 20 minutes before checking if fullscreen is needed.")
        time.sleep(1200)
        
        print("Check_fullscreen")
        check_fullscreen()


if __name__ == "__main__":
    main()
