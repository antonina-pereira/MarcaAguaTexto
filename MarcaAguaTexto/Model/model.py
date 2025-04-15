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

    # TODO Dev #1 - Criar m�todo para verificar se os dados enviados pela view est�o corretos
    # 1.1 verificar se o n�mero de recipientes n�o � superior a MAX_NUM_DESTINATARIOS
    # 1.2 verificar se o n�mero de espa�os no texto � pelo menos MIN_TEXT_SPACES
    def validar_dados(texto, num_destinatarios):
        pass

    def processar_dados(self):
        pass

    # TODO Dev #1 - Criar m�todo para criar um ficheiro .txt onde o texto com marca d'�gua ser� guardado
    def criar_ficheiro(self):
        pass

    # TODO Dev #1 - Criar m�todo para verificar se o ficheiro .txt onde o texto com marca d'�gua ser� guardado
    # foi criado corretamente
    # Este m�todo pode ser eliminado se a valida��o for feita no m�todo criar_ficheiro
    def validar_ficheiro(self):
        pass

    # TODO Dev #1 - Criar m�todo para escrever o texto com marca d'�gua num ficheiro .txt
    def escrever_ficheiro(self):
        pass

    # TODO Dev #1 - Criar m�todo para verificar se o ficheiro .txt foi escrito corretamente
    # Este m�todo pode ser eliminado se a valida��o for feita no m�todo escrever_ficheiro
    def validar_escrita(self):
        pass

    def limpar_dados(self):
        pass