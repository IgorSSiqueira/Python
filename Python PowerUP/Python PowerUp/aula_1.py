# Primeira Aula - RPA - Robot Programing 

# Passo 1 Acessar o sistema da empresa
#   https://dlp.hashtagtreinamentos.com/python/intensivao/login

#pip install pyautogui
# pip install pandas numpy openpyxl

import pyautogui
import time

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' 

pyautogui.PAUSE = 0.65
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')

#Passo 2 - Fazer Login
time.sleep(2)
# pyautogui.click(x=2449, y=428) #mudar
pyautogui.press('tab')
pyautogui.write('email@email.com')
pyautogui.press('tab')
pyautogui.write('aoisdao@@oasd#@##')
pyautogui.press('tab')
pyautogui.press('enter')

#Passo 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')
time.sleep(2)

#Passo 4 - Cadastrar um produto
#Passo 5 - Repetir
pyautogui.PAUSE = 0.1
for linha in tabela.index:
    pyautogui.click(x=843, y=258)
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):   
        pyautogui.write(obs)        
    
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(1000)
    time.sleep(0.5)




