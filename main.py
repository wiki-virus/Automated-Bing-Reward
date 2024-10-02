import pyautogui
import time
import random
import string
import subprocess
import os
import pygetwindow as gw
import keyboard

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"



print("Switch to personal if havent already.")


def generate_random_word(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


time.sleep(5)


def search(profile_number):
    for _ in range(30):
        print('Search no : ',(_+1))
        word = generate_random_word()
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write(word, interval=0.1)
        pyautogui.press('enter')
        time.sleep(6)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        if keyboard.is_pressed('n') or keyboard.is_pressed('N'):
            print(f"Skipping Profile {profile_number} after {_ + 1} searches...")
            return  # Exit the function and move to the next profile



for i in range (1,4):
    print('Profile no : ',i)
    profile_path = f"C:\\Users\\<YourUsername>\\AppData\\Local\\Microsoft\\Edge\\User Data\\Profile {i}"
    subprocess.Popen([edge_path, f"--user-data-dir={os.path.dirname(profile_path)}", f"--profile-directory=Profile {i}"])

    
    edge_windows = [w for w in gw.getWindowsWithTitle('Edge') if w.isActive is False]
    if edge_windows:
        edge_windows[0].activate()  # Activate the first inactive Edge window

    time.sleep(1)
    search(i)
    print('Onto next or Exit.')
    pyautogui.hotkey('alt', 'f4') #change to close the browser
    pyautogui.press('enter')
    time.sleep(1)

profile_path = r"C:\Users\<YourUsername>\AppData\Local\Microsoft\Edge\User Data\Default"
subprocess.run([edge_path, f"--user-data-dir={os.path.dirname(profile_path)}", f"--profile-directory={os.path.basename(profile_path)}"])
edge_windows = [w for w in gw.getWindowsWithTitle('Edge') if w.isActive is False]
if edge_windows:
    edge_windows[0].activate()  # Activate the first inactive Edge window

search('Default')
pyautogui.hotkey('alt', 'f4') #change to close the browser
pyautogui.press('enter')
