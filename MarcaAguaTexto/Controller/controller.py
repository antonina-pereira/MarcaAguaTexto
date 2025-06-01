from MarcaAguaTexto.Model.model import IModel
from MarcaAguaTexto.View.view import IView

from MarcaAguaTexto.Controller.wmk_controller_encoding import WmkControllerEncoding

# Classe Controller
class Controller:
    def __init__(self, model: IModel):
        """
        Inicializa o controlador com o modelo, a vista e o codificador.
        :param model: instância da classe Model
        :param view: instância da classe View
        """
        self.model = model
        self.model.adicionar_observador(self.evento_modelo)
        self.view = None
        self.encoder = WmkControllerEncoding()

    def evento_modelo(self, evento, **kwargs):
        """
        Método para lidar com eventos do modelo e notificar a vista.
        :param evento: evento disparado pelo modelo
        :param kwargs: argumentos adicionais do evento
        """
        codigo = kwargs.get("codigo", "")
        # Verifica o tipo de evento e chama o método correspondente na vista
        if evento == "dados_validos":
            self.view.mostrar_msg_dados_validos()
        elif evento == "erro_num_destinatarios":
            msg_erro = self.traduzir_erro_num_destinatarios(codigo)
            self.view.mostrar_msg_dados_invalidos(msg_erro)
            # Encerra o programa se os dados forem inválidos
            self.view.root.after(3000, self.programa_encerrado)
        elif evento == "erro_texto":
            msg_erro = self.traduzir_erro_texto(codigo)
            self.view.mostrar_msg_dados_invalidos(msg_erro)
            # Encerra o programa se os dados forem inválidos
            self.view.root.after(3000, self.programa_encerrado)
        elif evento == "erro_escrita":
            self.view.mostrar_msg_erro_na_codificacao()
            self.programa_encerrado()

    
    def traduzir_erro_num_destinatarios(self, codigo):
        if codigo == "NUM_DEST_NAO_NUMERO":
            return "Adicionar um número no campo dos destinatários."
        elif codigo == "NUM_DEST_FORA_INTERVALO":
            return "Número de destinatários tem de estar entre 1 e 509."
        else:
            return "Erro desconhecido no campo destinatários."

    def traduzir_erro_texto(self, codigo):
        if codigo == "ESPACOS_FORA_INTERVALO":
            return "Número de espaços no texto insuficiente."
        else:
            return "Erro desconhecido no texto."

    def traduzir_erro_escrita(self, codigo):
        if codigo == "ERRO_IO":
            return "Erro ao escrever o ficheiro."
        else:
            return "Erro desconhecido na codificação do texto."

    def set_view(self, view: IView):
        self.view = view

    # DEV2 - Alterei o espaçamento anterior para verificar a def abaixo. -- Nenhuma outra alteração
    def iniciar_programa(self):
        self.view.ativar_boas_vindas()
        self.view.run()

    def receber_dados_submetidos(self, texto, num_destinatarios):
        # # Valida os dados submetidos
        # if(not self.model.validar_dados(texto, num_destinatarios)):
        #     self.view.mostrar_msg_dados_invalidos()
        #     # Encerra o programa se os dados forem inválidos
        #     self.view.root.after(3000, self.programa_encerrado)
        #     return
        
        # self.view.mostrar_msg_dados_validos()

        # # Atualiza o Model
        # self.model.texto = texto.split("\n")
        # self.model.num_destinatarios = int(num_destinatarios)
        # # Inicia a codificação
        # self.codificar_texto()

        # Atualiza o Model (não chama diretamente métodos da View)
        self.model.texto = texto.split("\n")
        self.model.num_destinatarios = num_destinatarios
        # Valida e notifica via evento
        if not self.model.validar_dados(self.model.texto, self.model.num_destinatarios):
            self.model.notificar_observadores(evento="dados_invalidos")
            return
        self.model.notificar_observadores(evento="dados_validos")
        # Inicia a codificação (pode ser disparada por evento também, se preferir)
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
            self.model.notificar_observadores(evento="erro_escrita")
            # print(f"Erro na codificação: {e}")
            # self.programa_encerrado()

    def programa_encerrado(self):
        self.view.mostrar_msg_final()
        if hasattr(self.view, "root") and self.view.root is not None:
            self.view.root.after(3000, self.view.root.destroy)