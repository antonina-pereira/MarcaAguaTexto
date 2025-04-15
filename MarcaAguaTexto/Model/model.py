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

    def processar_dados(self):
        raise NotImplementedError

    def criar_ficheiros(self):
        raise NotImplementedError

    def validar_ficheiro(self):
        raise NotImplementedError

    def escrever_ficheiro(self):
        raise NotImplementedError

    def validar_escrita(self):
        raise NotImplementedError

    def limpar_dados(self):
        raise NotImplementedError

# Classe Model
class Model(IModel):
    def __init__(self, texto = None, num_destinatarios = 0):
        self.texto = texto if texto is not None else []
        self.num_destinatarios = num_destinatarios

    def obter_texto(self) -> list:
        return self.texto

    def obter_num_destinatarios(self) -> int:
        return self.num_destinatarios

    # TODO Dev #1 - Criar método para verificar se os dados enviados pela view estão corretos
    # 1.1 verificar se o número de recipientes não é superior a MAX_NUM_DESTINATARIOS
    # 1.2 verificar se o número de espaços no texto é pelo menos MIN_TEXT_SPACES
    def validar_dados(texto, num_destinatarios):
        pass

    def processar_dados(self):
        pass

    # TODO Dev #1 - Criar método para criar um ficheiro .txt onde o texto com marca d'água será guardado
    def criar_ficheiro(self):
        pass

    # TODO Dev #1 - Criar método para verificar se o ficheiro .txt onde o texto com marca d'água será guardado
    # foi criado corretamente
    # Este método pode ser eliminado se a validação for feita no método criar_ficheiro
    def validar_ficheiro(self):
        pass

    # TODO Dev #1 - Criar método para escrever o texto com marca d'água num ficheiro .txt
    def escrever_ficheiro(self):
        pass

    # TODO Dev #1 - Criar método para verificar se o ficheiro .txt foi escrito corretamente
    # Este método pode ser eliminado se a validação for feita no método escrever_ficheiro
    def validar_escrita(self):
        pass

    def limpar_dados(self):
        pass