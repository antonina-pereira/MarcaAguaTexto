from MarcaAguaTexto.model.model import IModel

# Interface da classe View
class IView:
    def ativar_boas_vindas(self):
        raise NotImplementedError

    def rotulo_prompt(self):
        raise NotImplementedError

    def digitar_dados(self):
        raise NotImplementedError

    def chegou_dados(self):
        raise NotImplementedError

    def rotulo_dados(self):
        raise NotImplementedError

    def submeter_dados(self):
        raise NotImplementedError

    def dados_submetidos(self):
        raise NotImplementedError

    def mensagem_em_curso(self):
        raise NotImplementedError

    def validar_dados(self):
        raise NotImplementedError

    def codificacao_terminou(self):
        raise NotImplementedError

    def mensagem_sucesso(self):
        raise NotImplementedError

    def mensagem_dados_validos(self):
        raise NotImplementedError

    def mensagem_dados_invalidos(self):
        raise NotImplementedError

# Classe View
class View(IView):
    def __init__(self, model: IModel):
        self.model = model
 
    # TODO Dev #2 - Substituir o print pelo ecrã de boas-vindas/inicial da aplicação
    def ativar_boas_vindas(self):
        print("Bem-vindo!")

    # TODO Dev #2 - Criar o input visual do texto e número de destinatários
    def rotulo_prompt(self):
        pass

    # TODO Dev #2 - Guardar os dados introduzidos pelo utilizador
    def digitar_dados(self):
        novo_texto = None
        self.model.texto = novo_texto
        novo_num_destinatarios = 0
        self.model.num_destinatarios = novo_num_destinatarios

    def chegou_dados(self):
        pass

    def rotulo_dados(self):
        pass

    def submeter_dados(self):
        pass

    def dados_submetidos(self):
        pass

    def mensagem_em_curso(self):
        pass

    def validar_dados(self):
        pass

    def codificacao_terminou(self):
        pass

    def mensagem_sucesso(self):
        pass

    def mensagem_dados_validos(self):
        pass

    def mensagem_dados_invalidos(self):
        pass
