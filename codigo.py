# Passo 1: Entrar no sistema da empresa
# Passo 2: fazer login
# Passo 3: Abrir base de dados
# Passo 4: Cadastrar 1 produto
# passo 5: Repetir passo 4 até acabar os produtos

import pyautogui
import time

pyautogui.PAUSE = 1
email = "pythonimpressionador@gmail.com"
senha = "sua senha muito muito muito dificilima"
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

# Fazer uma pausa maior para o site carregar
time.sleep(3)

pyautogui.click(x=712, y=510)
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

# Fazer uma pausa maior para o site carregar
time.sleep(3)

# Passo 3
import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # Passo 4
    pyautogui.click(x=945, y=370) # clica no campo do código
    # código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o proximo campo
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preço
    preço = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preço)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # passar para o botão enviar
    pyautogui.press("enter")
    # voltar para o inicio da pagina
    pyautogui.scroll(5000)

# Passo 5