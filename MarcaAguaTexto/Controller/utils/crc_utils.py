"""
Utilitário para cálculo de CRC-8 (Cyclic Redundancy Check).

Autor: Carlos Romão (Desenvolvedor #3)
Data: 15 de Abril 2025

Descrição:
Este módulo fornece uma função para gerar checksums CRC-8 a partir de strings binárias,
usando a biblioteca externa `crcmod`.
"""

import crcmod


def compute_crc8(binary_str: str) -> str:
    """
    Calcula o checksum CRC-8 de uma string binária.

    Parâmetros:
    - binary_str (str): sequência binária (ex: '101010101')

    Retorna:
    - str: checksum de 8 bits (ex: '11010110')
    """
    # Converte a string binária para bytes
    byte_data = int(binary_str, 2).to_bytes((len(binary_str) + 7) // 8, byteorder='big')

    # Função CRC-8 padrão (polinómio 0x07)
    crc8_func = crcmod.predefined.mkCrcFun('crc-8')
    crc_value = crc8_func(byte_data)

    # Formata o valor como string binária de 8 bits
    return format(crc_value, '08b')