# -*- coding: utf-8 -*-
"""
Testes unitários para a classe WmkControllerEncoding.

Autor: Carlos Romão (Desenvolvedor #3)
Data: 16 Abril 2025
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from Controller.wmk_controller_encoding import WmkControllerEncoding
import pytest



@pytest.fixture
def encoder():
    return WmkControllerEncoding()

def test_binary_converter_valido(encoder):
    # CA004: Converter número válido para binário
    # CA005: Converter número mínimo para binário (0)
    assert encoder.binary_converter(0) == "000000000"
    assert encoder.binary_converter(42) == "000101010"
    assert encoder.binary_converter(510) == "111111110"

def test_binary_converter_invalido(encoder):
    # CA006: Lançar erro ao converter número inválido (-1)
    # CA007: Lançar erro ao converter número inválido (limite++)
    with pytest.raises(ValueError):
        encoder.binary_converter(-1)
    with pytest.raises(ValueError):
        encoder.binary_converter(511)

def test_error_detection_output(encoder):
    # CF006: Validar aplicação correta do CRC-8
    binario = "000101010"
    crc = encoder.error_detection(binario)
    assert isinstance(crc, str)
    assert len(crc) == 8
    assert all(c in "01" for c in crc)

def test_encode_binary_into_text_sucesso(encoder):
    # CF007: Validar codificação correta dos espaços e espaços ininterruptos
    texto = "A " * 40  # 40 espaços
    binario = encoder.binary_converter(42)
    codificado = encoder.encode_binary_into_text(texto, binario)
    assert isinstance(codificado, str)
    assert len(codificado) == len(texto)

def test_encode_binary_into_text_erro(encoder):
    # CA012: Erro ao codificar texto com poucos espaços
    texto = "A " * 5  # poucos espaços
    binario = encoder.binary_converter(42)
    with pytest.raises(ValueError):
        encoder.encode_binary_into_text(texto, binario)
