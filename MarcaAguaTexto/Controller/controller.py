from Model.model import IModel
from View.view import IView

from Controller.wmk_controller_encoding import WmkControllerEncoding
import os

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
        self.output_directory = "Saida"  # Tester: Diretório de saída para os ficheiros codificados

    # [Alteração DEV3 - Corrigido método duplicado]
    def codificar_texto(self):
        """
        Executa o processo de codificação do texto para todos os destinatários,
        utilizando espaços e espaços ininterruptos para representar os bits.

        Para cada destinatário:
        - Converte o número para binário (9 bits)
        - Codifica o texto com o binário, marcadores e CRC
        - Gera um ficheiro .txt separado para cada destinatário com o texto codificado

        Em caso de erro, chama a view para notificar falha.

        [Nota DEV3 - Provisório]
        Esta geração de ficheiros é provisória para validação da codificação.
        Posteriormente será integrada de forma oficial no Model pela equipa.
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

                # NOVO: Cria um ficheiro de texto separado para cada destinatário
                # TESTER: Usa a pasta definida na classe. Se não existir, cria
                os.makedirs(self.output_directory, exist_ok=True)
                nome_ficheiro = os.path.join(self.output_directory, f"destinatario_{destinatario}.txt")
                with open(nome_ficheiro, "w", encoding="utf-8") as f:
                    f.write(texto_codificado)

                # Mostra uma parte do texto codificado no terminal (para testes)
                print(f"[Destinatário {destinatario}] Ficheiro '{nome_ficheiro}' criado com texto codificado.")
                print(texto_codificado[:100] + "...\n")

            # Notifica sucesso à vista
            self.view.mensagem_sucesso()

        except Exception as e:
            print(f"Erro na codificação: {e}")
            self.view.mensagem_dados_invalidos()

    # DEV2 - Alterei o espaçamento anterior para verificar a def abaixo. -- Nenhuma outra alteração
    def iniciar_programa(self):
        self.view.ativar_boas_vindas()
        self.view.run()

    def ativar_prompt(self):
        pass

    def dados_validos(self):
        pass

    def dados_invalidos(self):
        pass

    def programa_encerrado(self):
        pass