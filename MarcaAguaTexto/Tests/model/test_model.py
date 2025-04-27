'''
Testes do componente Model.
Este módulo verifica as funcionalidades de validação de dados,
criação e manipulação de arquivos implementadas no Model.

Tipo de testes: CAIXA ABERTA (White Box) e INTEGRAÇÃO DE BAIXO PARA CIMA (Bottom-Up)
'''

# -*- coding: utf-8 -*-

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

def test_validar_dados_zero_destinatarios():
    # CF004: Testar número de destinatários inferior a 1
    texto = ["texto com espaços suficientes"]
    num_destinatarios = 0
    modelo = Model()
    assert modelo.validar_dados(texto, num_destinatarios) is False

def test_validar_dados_texto_vazio():
    # CA013: Validar dados com texto vazio
    texto = []
    num_destinatarios = 5
    modelo = Model()
    assert modelo.validar_dados(texto, num_destinatarios) is False

def test_validar_dados_apenas_espacos():
    # CA014: Validar texto com apenas espaços em branco
    texto = [" " * 40]  # 40 espaços seguidos (mais que MIN_TEXT_SPACES=35)
    num_destinatarios = 5
    modelo = Model()
    assert modelo.validar_dados(texto, num_destinatarios) is True

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

def test_escrever_ficheiro_sem_texto():
    # CA015: Tentar escrever ficheiro sem texto definido no model
    modelo = Model(texto=[])
    modelo.criar_ficheiro()
    try:
        resultado = modelo.escrever_ficheiro()
        assert resultado is False
    except Exception:
        # Se lançar exceção, o teste também passa
        assert True
    
    # Limpar ficheiro se criado
    if os.path.exists("saida_marca_agua.txt"):
        os.remove("saida_marca_agua.txt")

def test_escrever_texto_caracteres_especiais():
    # CA017: Codificar texto com caracteres especiais
    texto = ["Texto com acentuação: é à ç ã õ", "Símbolos: € £ $ ¢ © ®", "Emojis: 😀 👍 🚀"]
    modelo = Model(texto=texto)
    modelo.criar_ficheiro()
    
    try:
        resultado = modelo.escrever_ficheiro()
        assert resultado is True
        assert modelo.validar_escrita() is True
    except UnicodeEncodeError:
        # Se falhar com erro de codificação, o teste apenas registra isso
        assert False, "Falhou com erro de codificação UTF-8"
    finally:
        # Limpar ficheiro
        if os.path.exists("saida_marca_agua.txt"):
            os.remove("saida_marca_agua.txt")
