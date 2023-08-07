#Bibliotecas comandos
import pyautogui
import pandas as pd
import time
#pyautogui.write - escrever um texto
#pyautogui.press - pressioanr uma tecla
#pyautogui.click - clicar em uma posição na tela
pyautogui.PAUSE = 5

#Passo a passo do projeto
#Passo 1 - Entar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login


#abrir o navegador (Edge)
pyautogui.press("win")
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")
#Entar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)



#Passo 2 - Fazer login
#selecionar o campo do e-mail
pyautogui.click(x=750, y=451)
#digitar o e-mail
pyautogui.write("vht@hotmail.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("tab")
pyautogui.press("enter")


#Passo 3 - Importar a base de produtos para cadastrar

tabela = pd.read_csv("produtos.csv")
print(tabela)

#Passo 4 - Cadastrar um produto

for linha in tabela.index:
    #clicar no campo do código
    pyautogui.click(x=721, y=313)
    #pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    #preencher o campo
    pyautogui.write(str(codigo))
    #passar para o próximo campo
    pyautogui.press("tab")
    #preencher o campo
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela[linha, "obs"]))
        pyautogui.press("tab")
        pyautogui.press("enter") #cadastra o produto - botao enviar
    #dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    #Passo 5 - Repetir o processo de cadastro até o fim