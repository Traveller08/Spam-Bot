import pyautogui
import time

a=int(pyautogui.prompt("How many times you want to send a message"))
mess=pyautogui.prompt("Enter the message you want to send")
pyautogui.confirm("Are you sure?")
pyautogui.alert("The Bot is going to start, please move the cursor to the target area in 5 sec")
time.sleep(8)
x,y=pyautogui.position()
pyautogui.moveTo(x,y)
pyautogui.click()
while(a>0):
    pyautogui.write(mess)
    pyautogui.press('enter')
    a-=1
