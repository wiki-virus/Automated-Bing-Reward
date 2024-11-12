import os
import random
import string
import subprocess
import time
from asyncio import timeout
from logo import logo
import keyboard
import pyautogui
import pygetwindow as gw
from inputimeout import inputimeout, TimeoutOccurred

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
extra_profile_count=0 #if you have more profiles change 0 to your desired one
preference = 1
check_url="https://rewards.bing.com/"
check_state=False

print(logo)

check_state=bool(int(input(f"Enter which mode to open.\n ├─ 1 - Search (Default) \n └─ 2 - Points query\n\n"))-1)

def clear_console():
    os.system('cls')
clear_console()
def generate_random_word(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def search(profile_number):
    for _ in range(30):
        time.sleep(1)
        print('Search no : ',(_+1))
        word = generate_random_word()
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write(word, interval=0.1)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)
        if keyboard.is_pressed('n') or keyboard.is_pressed('N'):
            print(f"Skipping Profile {profile_number} after {_ + 1} searches...")
            return  
if not check_state:
    try:
        preference= int(inputimeout(prompt=f"Enter starting point if prefered ( Default/ Peronal can be mentioned by '{extra_profile_count+1}'. ", timeout=5))

    except TimeoutOccurred:
        pass

    finally:
        print("Starting from :", preference,end='\n')
    print("end")

    for i in range (preference,(extra_profile_count+1)):
        edge_windows = [w for w in gw.getWindowsWithTitle('Edge') if w.isActive is False]
        time.sleep(0.5)
        print('Profile no : ',i)
        profile_path = f"C:\\Users\\rosha\\AppData\\Local\\Microsoft\\Edge\\User Data\\Profile {i}"
        subprocess.Popen([edge_path, f"--user-data-dir={os.path.dirname(profile_path)}", f"--profile-directory=Profile {i}"])


        time.sleep(1)
        search(i)
        print('Onto next or Exit.')
        pyautogui.hotkey('alt', 'f4')
        pyautogui.press('enter')
        time.sleep(1)


    profile_path = r"C:\Users\rosha\AppData\Local\Microsoft\Edge\User Data\Default"
    subprocess.run([edge_path, f"--user-data-dir={os.path.dirname(profile_path)}", f"--profile-directory={os.path.basename(profile_path)}"])
    edge_windows = [w for w in gw.getWindowsWithTitle('Edge') if w.isActive is False]
    time.sleep(0.5)
    search('Default')
    pyautogui.hotkey('alt', 'f4')
    pyautogui.press('enter')

else:
    print("Points query mode")
    for i in range((extra_profile_count),0,-1):
        subprocess.Popen([edge_path, f"--profile-directory=Profile {i}", check_url])
        time.sleep(0.25)
    subprocess.Popen([edge_path, f"--profile-directory=Default", check_url])
