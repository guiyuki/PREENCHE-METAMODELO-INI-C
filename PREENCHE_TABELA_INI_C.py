import pyautogui
import time
import csv

'''
Arquivo para ler um csv e preenhcer o metamodelo da INI-C da PBE Edifica.
Criar um arquivo .csv somente com os valores.
Deixar o script e o arquivo na mesma pasta.
Possiveis erros.
'''

def escrevevalor(lista=list):
    for i in range(len(lista)):
        VALOR=lista[i]
        if (i==7 or i==8) and (VALOR=='S' or VALOR=='s'):
            VALOR="ss"
            pass
        elif VALOR=='Perimetral':
            VALOR='P'
            pass
        if VALOR=='p':
            pyautogui.hotkey('tab')
            time.sleep(0.02)
            break
        elif VALOR=='':
            break
        elif i==1 and VALOR!='':
            pyautogui.hotkey('tab')
            time.sleep(0.02)
            pyautogui.write(VALOR, interval=0.005)
            time.sleep(0.02)
            pyautogui.hotkey('tab')
            pass
        elif i==(len(lista)-1):
            pyautogui.write(VALOR, interval=0.005)
            time.sleep(0.02)
            pyautogui.hotkey('tab')
        else:
            pyautogui.write(VALOR, interval=0.005)
            time.sleep(0.02)
            pyautogui.hotkey('tab')
            pass
        pass
    pass

#codigo

def executar():
    arquivo =  open(input('Nome do arquivo .csv\n O arquivo deve estar na mesma pasta que esse arquivo! \n USAR UMA VEZ PARA CADA PAVIMENTO!!\nDEVE CONTER O NOME EXATO DO ARQUIVO SENSÍVEL ÀS minúsculas!!!\n')+ ".csv")
    data = csv.reader(arquivo,delimiter=';')
    linha =[]
    pyautogui.hotkey('alt','tab')
    for row in data:
        escrevevalor(row)
        pass
    pyautogui.hotkey('alt','tab')

executar()
executar()
executar()

