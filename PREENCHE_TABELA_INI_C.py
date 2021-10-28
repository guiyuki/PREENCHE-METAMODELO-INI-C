import pyautogui
import time
import csv

'''
Arquivo para ler um csv e preenhcer o metamodelo da INI-C da PBE Edifica.
Criar um arquivo .csv somente com os valores.
Deixar o script e o arquivo na mesma pasta.
Possiveis erros.
'''

def executar():
    arquivo =  open(input('Nome do arquivo .csv\n O arquivo deve estar na mesma pasta que esse arquivo! \n USAR UMA VEZ PARA CADA PAVIMENTO!!\nDEVE CONTER O NOME EXATO DO ARQUIVO SENSÍVEL ÀS minúsculas!!!\n')+ ".csv")
    data = csv.reader(arquivo,delimiter=';')
    linha = data.line_num
    pyautogui.hotkey('alt','tab')
    for row in data:
        escrevevalor(row,linha)
        pass
    pyautogui.hotkey('alt','tab')
    pass
pass

def escrevevalor(lista=list,linha=int):
    for i in range(len(lista)):
        VALOR=lista[i]
        #regras para linhas
        #linha Fator Solar Vidro
        if linha==9 and VALOR=='':
            VALOR=str(0.5)
            pass
        #linha Uvidro
        if linha==10 and VALOR=='':
            VALOR=str(4)
            pass
        #linha tipo de zona - interna/perimetral
        elif linha==5 and VALOR=='p':
            VALOR='P'
            pass
        elif (i==7 or i==8) and (VALOR=='S' or VALOR=='s'):
            VALOR="ss"
            pass
        elif VALOR=='Perimetral' or VALOR=='perimetral':
            VALOR='P'
            pass
        #escrever
        if i==1 and VALOR!='':
            pyautogui.hotkey('tab')
            escrever(VALOR)
        else:
            escrever(VALOR)
        pass
    pass
pass

def escrever(var=str):
    V=.03
    if var=='':
        pass
    elif var=='p':
        time.sleep(V)
        pyautogui.hotkey('tab')
        pass
    else:
        pyautogui.write(var, interval=0.005)
        time.sleep(V)
        pyautogui.hotkey('tab')
        print(var)
        pass
    pass
pass

    

#codigo



executar()
executar()
executar()

