import pyautogui              # Importando pyautogui
from time import sleep        # Importando função sleep do módulo time

pyautogui.PAUSE = 1           # Tempo entre uma ação e outra
pyautogui.press('win')        # Pressionar o botão "windows"
pyautogui.write('chrome')     # Digitar "chrome"
pyautogui.press('enter')      # Apertar Enter
sleep(3)  # ------------------- Aguardar 3 segundos (somente 1 vez)
pyautogui.write('https://github.com/thiagoperini')  # Digitar meu endereço de repositório
pyautogui.press('enter')  # ---- Apertar Enter
