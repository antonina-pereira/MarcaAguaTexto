# -*- coding: utf-8 -*-


''' TODO Verificador
test_controller_methods.py
Ficheiro que contém testes para verificar o
comportamento dos métodos do componente controller'''

import pytest

from unittest.mock import MagicMock

import MarcaAguaTexto.Controller.controller
import MarcaAguaTexto.Controller.wmk_controller_encoding

# Teste para a conversão do número do destinatário no código binário
def test_binary_converter():
    # CA004: Converter número válido para binário
    pass

# Teste para gerar o código CRC-8 a partir de uma string binária
def test_error_detection():
    # CF006: Validar aplicação correta do CRC-8
    pass

# Teste para a substituir os espaços por texto por espaços ou espaços ininterruptos
def test_encode_binary_into_text():
    # CF007: Validar codificação correta dos espaços e espaços ininterruptos
    pass

# Teste para a codificação do texto
def test_codificar_texto():
    # CA011: Codificar texto com binário válido
    pass
