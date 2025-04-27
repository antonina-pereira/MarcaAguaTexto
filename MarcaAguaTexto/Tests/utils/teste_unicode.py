'''
Utilitário de diagnóstico para análise de codificação Unicode.
Este módulo permite verificar como os caracteres Unicode (especialmente espaços
normais e ininterruptos) estão a ser codificados nos arquivos de saída.

Tipo de testes: FERRAMENTA DE SUPORTE AOS TESTES DE CAIXA FECHADA
'''

import os

def test_caracteres_unicode():
    # CF007: Validar codificação correta dos espaços e espaços ininterruptos
    # Caminho para o ficheiro de teste
    caminho = os.path.join(os.path.dirname(__file__), "../../Saida/destinatario_0.txt")
    
    if not os.path.exists(os.path.abspath(caminho)):
        print("Ficheiro não encontrado. Execute primeiro os testes de codificação.")
        return
        
    with open(os.path.abspath(caminho), "r", encoding="utf-8") as f:
        texto = f.read()
    
    espacos_normais = 0
    espacos_ininterruptos = 0
    
    for i, char in enumerate(texto):
        if char == " ":
            espacos_normais += 1
            print(f"Posição {i}: ' ' - Unicode {ord(char)} (espaço normal)")
        elif char == "\u00A0":
            espacos_ininterruptos += 1
            print(f"Posição {i}: '{char}' - Unicode {ord(char)} (espaço ininterrupto)")
    
    print(f"Total: {espacos_normais} espaços normais, {espacos_ininterruptos} espaços ininterruptos")
    
    # Verificação opcional
    assert espacos_normais > 0 or espacos_ininterruptos > 0, "Nenhum espaço encontrado no texto"

if __name__ == "__main__":
    test_caracteres_unicode()
