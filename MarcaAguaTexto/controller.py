from model import IModel
from view import IView

# Classe controller
class Controller:
    def __init__(self, model: IModel, view: IView):
        self.model = model
        self.view = view

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