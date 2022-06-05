import cv2
import time
import pyautogui


time.sleep(3)
while True:
    print('searching begin')
    while pyautogui.locateOnScreen('./image/begin.png', confidence=0.9) == None:
        pass
    begin_bottom = pyautogui.locateOnScreen('./image/begin.png', confidence=0.9)
    pyautogui.click(begin_bottom)
    
    for i in range(3):
        print('searching', i+1)
        while pyautogui.locateOnScreen('./image/choice'+str(i+1)+'.png', confidence=0.9) == None:
            pass
        choice_bottom = pyautogui.locateOnScreen('./image/choice'+str(i+1)+'.png', confidence=0.9)
        pyautogui.click(choice_bottom)
        time.sleep(1)
        pyautogui.click(921, 564)
        print('searching ok', i+1)
        while pyautogui.locateOnScreen('./image/ok2.png', confidence=0.8) == None:
            pass
        ok1_bottom = pyautogui.locateOnScreen('./image/ok2.png', confidence=0.8)
        pyautogui.click(ok1_bottom)
        time.sleep(10)

    print('searching ok sort')
    while pyautogui.locateOnScreen('./image/ok2.png', confidence=0.9) == None:
        pass
    ok1_bottom = pyautogui.locateOnScreen('./image/ok2.png', confidence=0.9)
    pyautogui.click(ok1_bottom)
    time.sleep(5)
    print('searching ok final')
    while pyautogui.locateOnScreen('./image/ok2.png', confidence=0.9) == None:
        pyautogui.press('space')
        pyautogui.press('j')
        pyautogui.press('k')

    ok2_bottom = pyautogui.locateOnScreen('./image/ok2.png', confidence=0.9)
    pyautogui.click(ok2_bottom)





