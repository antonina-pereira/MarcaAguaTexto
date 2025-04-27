# teste_unicode.py
import os

# Ler o texto de um ficheiro e imprimir os códigos Unicode dos espaços
caminho = os.path.join(os.path.dirname(__file__), "../../destinatario_0.txt")

with open(os.path.abspath(caminho), "r", encoding="utf-8") as f:
    texto = f.read()

for i, char in enumerate(texto):
    if char == " " or char == "\u00A0":
        print(f"Posição {i}: {repr(char)} - Unicode {ord(char)}")




