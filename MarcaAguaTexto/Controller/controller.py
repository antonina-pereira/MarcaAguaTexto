from Model.model import IModel
from View.view import IView

from Controller.wmk_controller_encoding import WmkControllerEncoding

# Classe Controller
class Controller:
    def __init__(self, model: IModel, view: IView):
        """
        Inicializa o controlador com o modelo, a vista e o codificador.

        :param model: instância da classe Model
        :param view: instância da classe View
        """
        self.model = model
        self.view = view
        self.encoder = WmkControllerEncoding()

    def codificar_texto(self):
        """
        Executa o processo de codificação do texto para todos os destinatários,
        utilizando espaços e espaços ininterruptos para representar os bits.

        Para cada destinatário:
        - Converte o número para binário (9 bits)
        - Codifica o texto com o binário
        - (Para já) imprime o resultado no terminal
        - (Futuramente) delega a criação de ficheiros ao model

        Em caso de erro, chama a view para notificar falha.
        """
        try:
            # Obtém o texto original como string (a partir de uma lista de palavras)
            texto_original = " ".join(self.model.obter_texto())
            num_destinatarios = self.model.obter_num_destinatarios()

            for destinatario in range(num_destinatarios):
                # Gera binário de 9 bits para o número do destinatário
                binario = self.encoder.binary_converter(destinatario)

                # Codifica o texto com o binário, marcadores e CRC
                texto_codificado = self.encoder.encode_binary_into_text(texto_original, binario)

                # Mostra uma parte do texto codificado no terminal (para testes)
                print(f"[Destinatário {destinatario}] Texto codificado:")
                print(texto_codificado[:100] + "...\n")

            # Notifica sucesso à vista
            self.view.mensagem_sucesso()

        except Exception as e:
            print(f"Erro na codificação: {e}")
            self.view.mensagem_dados_invalidos()










































    def iniciar_programa(self):
        self.view.ativar_boas_vindas()

    def ativar_prompt(self):
        pass

    def dados_validos(self):
        pass

    def dados_invalidos(self):
        pass

    def codificar_texto(self):
        pass

    def programa_encerrado(self):
        pass