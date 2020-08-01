import os
import pyautogui
import time
import schedule
import getpass

user  = getpass.getuser()

code1 = ('')
passw1 = ('')
time1 = ('00:00')

code2 = ('')
passw2 = ('')
time2 = ('00:00')

code3 = ('')
passw3 = ('')
time3 = ('00:00')

code4 = ('')
passw4 = ('')
time4 = ('00:00')

code5 = ('')
passw5 = ('')
time5 = ('00:00')

def class0(code, passw):
   os.system("TASKKILL /F /IM Zoom.exe")
   os.popen('C:/Users/{}/AppData/Roaming/Zoom/bin/Zoom.exe'.format(user)) #Caminho padrão
   time.sleep(5)
   x,y = pyautogui.locateCenterOnScreen('join.png')
   pyautogui.click(x, y)
   time.sleep(5)
   pyautogui.write(str(code))
   pyautogui.press('enter')
   time.sleep(5)
   pyautogui.write(str(passw))
   pyautogui.press('enter')
 
schedule.every().day.at(time1).do(class0, code=code1, passw=passw1)
schedule.every().day.at(time2).do(class0, code=code2, passw=passw2)
schedule.every().day.at(time3).do(class0, code=code3, passw=passw3)
schedule.every().day.at(time4).do(class0, code=code4, passw=passw4)
schedule.every().day.at(time5).do(class0, code=code5, passw=passw5)

while True:
    schedule.run_pending()
    time.sleep(1)
