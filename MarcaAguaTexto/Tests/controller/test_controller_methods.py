'''
Testes do componente Controller.
Este módulo verifica se o Controller coordena corretamente as interações
entre os componentes Model e View, garantindo o fluxo adequado de dados.

Tipo de testes: INTEGRAÇÃO DE CIMA PARA BAIXO (Top-Down)
'''

import pytest

from unittest.mock import MagicMock

import MarcaAguaTexto.Controller.controller
import MarcaAguaTexto.Controller.wmk_controller_encoding