import os
from abc import ABC, abstractmethod

MAX_NUM_DESTINATARIOS = 510

MIN_TEXT_SPACES = 35

# Interface da classe Model
class IModel(ABC):
    @abstractmethod
    def obter_texto(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def obter_num_destinatarios(self) -> int:
        raise NotImplementedError

    def validar_dados(self):
        raise NotImplementedError

    def escrever_ficheiro(self):
        raise NotImplementedError

# Classe Model
class Model(IModel):
    def __init__(self, texto = None, num_destinatarios = 0, output_directory="MarcaAguaTexto/Saida"):
        self.texto = texto if texto is not None else []
        self.num_destinatarios = num_destinatarios
        self.output_directory = output_directory
        self._observadores = []

    def adicionar_observador(self, callback):
        self._observadores.append(callback)

    def notificar_observadores(self, evento, **kwargs):
        for callback in self._observadores:
            callback(evento, **kwargs)

    def obter_texto(self) -> list:
        return self.texto

    def obter_num_destinatarios(self) -> int:
        return self.num_destinatarios

    # TODO Dev #1 - Criar método para verificar se os dados enviados pela view estão corretos
    # 1.1 verificar se o número de recipientes não é superior a MAX_NUM_DESTINATARIOS
    # 1.2 verificar se o número de espaços no texto é pelo menos MIN_TEXT_SPACES
    def validar_dados(self, texto, num_destinatarios):
        # Verifica se num_destinatarios é um número
        try:
            num_destinatarios_int = int(num_destinatarios)
        except Exception:
            #return False
            self.notificar_observadores(evento="erro_num_destinatarios", codigo="NUM_DEST_NAO_NUMERO")
            return False

        self.num_destinatarios = num_destinatarios_int
        
        if not (1 <= num_destinatarios_int < MAX_NUM_DESTINATARIOS):
            self.notificar_observadores(evento="erro_num_destinatarios", codigo="NUM_DEST_FORA_INTERVALO")
            return False

        num_espacos = sum(linha.count(" ") for linha in texto)
        if num_espacos < MIN_TEXT_SPACES:
            self.notificar_observadores(evento="erro_texto", codigo="ESPACOS_FORA_INTERVALO")
            return False

        self.notificar_observadores(evento="dados_validos")
        return True

    # TODO Dev #1 - Criar método para criar um ficheiro .txt onde o texto com marca d'água será guardado
    def escrever_ficheiro(self, destinatario, texto_codificado):
        try:
            os.makedirs(self.output_directory, exist_ok=True)
            nome_ficheiro = os.path.join(self.output_directory, f"destinatario_{destinatario}.txt")
            with open(nome_ficheiro, "w", encoding="utf-8") as f:
                f.write(texto_codificado)
                # Mostra uma parte do texto codificado no terminal (para testes)
                print(f"[Destinatário {destinatario}] Ficheiro '{nome_ficheiro}' criado com texto codificado.")
                print(texto_codificado[:100] + "...\n")
        except Exception as e:
            self.notificar_observadores(evento="erro_escrita", codigo="ERRO_IO")