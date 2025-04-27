import os
import pytest
from MarcaAguaTexto.Model.model import Model

def test_validar_dados_valido():
    # CA001: Validar texto com espaços suficientes
    texto = [
        "linha 1 com espaços entre palavras para testar corretamente a funcionalidade e passar no teste com mais de trinta e cinco espaços.",
        "linha 2 ainda mais espaços para garantir que temos mais que suficiente no total, mesmo que o texto não faça muito sentido."
    ]
    num_destinatarios = 100
    modelo = Model()
    assert modelo.validar_dados(texto, num_destinatarios) is True

def test_validar_dados_excesso_destinatarios():
    # CA003: Validar número de destinatários acima do limite
    texto = ["texto com espaços suficientes"]
    num_destinatarios = 1000
    modelo = Model()
    assert modelo.validar_dados(texto, num_destinatarios) is False

def test_validar_dados_poucos_espacos():
    # CA002: Validar texto com espaços insuficientes
    texto = ["sem_espacos"]
    num_destinatarios = 10
    modelo = Model()
    assert modelo.validar_dados(texto, num_destinatarios) is False

def test_criar_e_validar_ficheiro():
    # CA009: Criar e validar ficheiro de saída
    modelo = Model()
    assert modelo.criar_ficheiro() is True
    assert modelo.validar_ficheiro() is True
    os.remove("saida_marca_agua.txt")

def test_escrever_e_validar_escrita():
    # CA010: Escrever e validar escrita em ficheiro
    texto = ["linha 1", "linha 2", "linha 3"]
    modelo = Model(texto=texto)
    modelo.criar_ficheiro()
    assert modelo.escrever_ficheiro() is True
    assert modelo.validar_escrita() is True
    os.remove("saida_marca_agua.txt")
