import random, pyautogui as pyauto

for i in range(15):
    h = random.randint(0, 900)
    w = random.randint(0, 1600)
    pyauto.click(h, w, duration=0.6)
    pyauto.hotkey('winleft', 'm')


