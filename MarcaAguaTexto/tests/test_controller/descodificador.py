# leitor_marca_agua_interpretador_crc.py

from Controller.utils.crc_utils import compute_crc8  # Importar função já existente

def ler_marca_agua_interpretar_validar_crc(ficheiro_txt):
    """
    Lê o texto codificado, extrai o binário, interpreta:
    - Confirma o marcador inicial
    - Extrai o número codificado
    - Confirma o marcador final
    - Compara o CRC-8 extraído com o recalculado

    Parâmetros:
    - ficheiro_txt (str): caminho para o ficheiro de texto codificado.

    Resultado:
    - Mostra no terminal o binário extraído, o número e a verificação de CRC.
    """
    try:
        # Abre o ficheiro para leitura
        with open(ficheiro_txt, "r", encoding="utf-8") as f:
            texto = f.read()

        # Variável para armazenar o binário reconstruído
        binario_extraido = ""

        for char in texto:
            if char == " ":
                binario_extraido += "0"
            elif char == "\u00A0":
                binario_extraido += "1"

        print("Binário extraído completo:")
        print(binario_extraido)

        if len(binario_extraido) < (9 + 9 + 9 + 8):
            print("Erro: Binário extraído demasiado curto para análise completa.")
            return

        # Dividir o binário conforme o protocolo
        marcador_inicio = binario_extraido[:9]
        numero_codificado = binario_extraido[9:18]
        marcador_fim = binario_extraido[18:27]
        crc_extraido = binario_extraido[27:35]

        print("\nInterpretação:")
        print(f"Marcador de Início: {marcador_inicio}")
        print(f"Número Codificado: {numero_codificado} (decimal: {int(numero_codificado, 2)})")
        print(f"Marcador de Fim: {marcador_fim}")
        print(f"CRC-8 extraído: {crc_extraido}")

        if marcador_inicio == "1" * 9 and marcador_fim == "1" * 9:
            print("\n✅ Marcadores de início e fim corretos!")
        else:
            print("\n⚠️ Marcadores incorretos! Pode haver erro na codificação ou no texto.")

        # Recalcular o CRC a partir do número codificado
        crc_recalculado = compute_crc8(numero_codificado)
        print(f"CRC-8 recalculado: {crc_recalculado}")

        # Comparar CRCs
        if crc_recalculado == crc_extraido:
            print("\n✅ CRC-8 validado com sucesso! Texto íntegro.")
        else:
            print("\n❌ CRC-8 diferente! Pode haver corrupção no texto ou erro na codificação.")

    except Exception as e:
        print(f"Erro ao ler ou interpretar a marca de água: {e}")


# Exemplo de chamada
if __name__ == "__main__":
    ler_marca_agua_interpretar_validar_crc("../../destinatario_0.txt")


