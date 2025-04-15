"""
Módulo de codificação binária e inserção de marca d'água invisível no texto.

Autor: Carlos Romão (Desenvolvedor #3)
Data: 15 Abril 2025

Descrição:
Este módulo contém as funções responsáveis por:
- Converter o número do destinatário num binário de 9 bits
- Gerar o CRC-8 do binário
- Inserir a marca binária no texto original, usando espaços e espaços ininterruptos
"""

from Controller.utils.crc_utils import compute_crc8

class WmkControllerEncoding:
    def __init__(self):
        # Marcador de início e fim (9 bits de 1)
        self.START_END_MARKER = '1' * 9
        # Tamanho do código binário principal (número do destinatário)
        self.CODE_BIT_SIZE = 9

    def binary_converter(self, recipient_number: int) -> str:
        """
        Converte o número do destinatário num binário de 9 bits.

        Parâmetros:
        - recipient_number (int): número entre 0 e 510

        Retorna:
        - str: representação binária com 9 bits
        """
        if not (0 <= recipient_number <= 510):
            raise ValueError("Recipient number must be between 0 and 510.")
        binary_string = format(recipient_number, f'0{self.CODE_BIT_SIZE}b')
        return binary_string

    def error_detection(self, binary_data: str) -> str:
        """
        Gera o código CRC-8 a partir de uma string binária.

        Parâmetros:
        - binary_data (str): string binária (ex: '000101010')

        Retorna:
        - str: checksum CRC-8 com 8 bits
        """
        return compute_crc8(binary_data)

    def encode_binary_into_text(self, text: str, binary_code: str) -> str:
        """
        Substitui espaços normais (' ') por:
        - ' ' → representa 0
        - ' ' (espaço ininterrupto) → representa 1

        A sequência codificada final contém:
        - Marcador de início (9 bits de 1)
        - Código binário do destinatário (9 bits)
        - Marcador de fim (9 bits de 1)
        - Código CRC-8 (8 bits)

        Parâmetros:
        - text (str): texto original com espaços suficientes
        - binary_code (str): código binário a inserir

        Retorna:
        - str: texto com marca d'água embutida

        Lança:
        - ValueError: se o texto não tiver espaços suficientes
        """
        full_code = self.START_END_MARKER + binary_code + self.START_END_MARKER
        crc = self.error_detection(binary_code)
        full_code += crc

        encoded_text = ""
        index = 0

        for char in text:
            if char == " " and index < len(full_code):
                encoded_text += " " if full_code[index] == '0' else " "
                index += 1
            else:
                encoded_text += char

        if index < len(full_code):
            raise ValueError("Texto insuficiente: espaços a menos para codificação.")
        return encoded_text