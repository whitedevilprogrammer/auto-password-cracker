import time
import os

#os.system("adb devices")
#os.system("adb shell")
    

asc = ['input tap 554 2221',
       'input tap 167 1782',
       'input tap 576 1804',
       'input tap 890 1804',
       'input tap 188 1927',
       'input tap 554 1927',
       'input tap 957 1927',
       'input tap 190 2121',
       'input tap 567 2121',
       'input tap 899 2121'] # adb_shell_command

#print(len(asc))

time.sleep(5)
for i in range(100000,999999):
    s = str(i)
    for j in s: # String to index number access the value !
        os.system('adb shell '+asc[int(j)])
        #print('adb shell '+asc[int(j)])
    print(i)
    time.sleep(1.5)


##time.sleep(5)
##for i in range(100000,999999):
##    s = str(i)
##    for j in s: # String to index number access the value !
##        pyperclip.copy(str(asc[int(j)]))
##        pyautogui.hotkey("ctrl","shift","v")
##        pyautogui.press("enter")
##    time.sleep(1.5)


    
    
