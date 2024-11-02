import pyautogui
import time

pyautogui.PAUSE = 0.5   

#pesquisa
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press(('enter'))

#google
pyautogui.click(x=-393, y=38)
pyautogui.write('hashtagtreinamentos.com')
pyautogui.press(('enter'))

#skip add
time.sleep(13)
pyautogui.moveTo(x=-337, y=260, duration= 1)
pyautogui.click()

#barra de pesquisa curso
pyautogui.moveTo(x=-965, y=107,duration=1)
pyautogui.click(x=-1087, y=272)

#descer
time.sleep(2)
pyautogui.scroll(-3000)
time.sleep(2)

#cadastro
pyautogui.moveTo(x=-527, y=564,duration=1)
pyautogui.click()
pyautogui.click(x=-561, y=444)
pyautogui.write('Andre Luiz')
pyautogui.press('tab')
pyautogui.write('juninhoreidelas@gmail.com')
pyautogui.press('tab')
pyautogui.write('37 999912345')
pyautogui.moveTo(x=-572, y=629,duration=1)