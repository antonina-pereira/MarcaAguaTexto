# -*- coding: utf-8 -*-


''' TODO Verificador
test_controller_methods.py
Ficheiro que cont�m testes para verificar o
comportamento dos m�todos do componente controller'''

import pytest

from unittest.mock import MagicMock

import MarcaAguaTexto.Controller.controller
import MarcaAguaTexto.Controller.wmk_controller_encoding

# Teste para a convers�o do n�mero do destin�rio no c�digo bin�rio
def test_binary_converter():
    # CA004: Converter número válido para binário
    pass

# Teste para gerar o c�digo CRC-8 a partir de uma string bin�ria
def test_error_detection():
    # CF006: Validar aplicação correta do CRC-8
    pass

# Teste para a subsituir os espa�os por texto por espa�os ou espa�os ininterruptos
def test_encode_binary_into_text():
    # CF007: Validar codificação correta dos espaços e espaços ininterruptos
    pass

# Teste para a codifica��o do texto
def test_codificar_texto():
    # CA011: Codificar texto com binário válido
    pass
