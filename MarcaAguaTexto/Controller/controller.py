from MarcaAguaTexto.Model.model import IModel
from MarcaAguaTexto.View.view import IView

from MarcaAguaTexto.Controller.wmk_controller_encoding import WmkControllerEncoding

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
        #self.output_directory = "Saida"  # Tester: Diretório de saída para os ficheiros codificados

    # DEV2 - Alterei o espaçamento anterior para verificar a def abaixo. -- Nenhuma outra alteração
    def iniciar_programa(self):
        self.view.ativar_boas_vindas()
        self.view.run()

    def receber_dados_submetidos(self, texto, num_destinatarios):
        # Valida os dados submetidos
        if(not self.model.validar_dados(texto, num_destinatarios)):
            self.view.mostrar_msg_dados_invalidos()
            # Encerra o programa se os dados forem inválidos
            self.view.root.after(3000, self.programa_encerrado)
            return
        
        self.view.mostrar_msg_dados_validos()

        # Atualiza o Model
        self.model.texto = texto.split("\n")
        self.model.num_destinatarios = int(num_destinatarios)
        # Inicia a codificação
        self.codificar_texto()

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
        """
        # Indicar ao utilizador que a codificação está em curso
        self.view.root.after(2000, self.view.mostrar_msg_em_curso)

        try:
          
            # Obtém o texto original como string (a partir de uma lista de palavras)
            texto_original = " ".join(self.model.obter_texto())
            num_destinatarios = self.model.obter_num_destinatarios()  

            for destinatario in range(num_destinatarios):
                # Gera binário de 9 bits para o número do destinatário
                binario = self.encoder.binary_converter(destinatario)

                # Codifica o texto com o binário, marcadores e CRC
                texto_codificado = self.encoder.encode_binary_into_text(texto_original, binario)

                self.model.escrever_ficheiro(destinatario, texto_codificado)  # Chama o método do Model para criar o ficheiro

            # Notifica sucesso à vista
            self.view.root.after(4000, self.view.mostrar_msg_sucesso)
            self.view.root.after(7000, self.programa_encerrado)
            return
            
        except Exception as e:
            print(f"Erro na codificação: {e}")
            self.programa_encerrado()

    def programa_encerrado(self):
        self.view.mostrar_msg_final()
        if hasattr(self.view, "root") and self.view.root is not None:
            self.view.root.after(3000, self.view.root.destroy)