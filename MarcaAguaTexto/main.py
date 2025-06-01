from MarcaAguaTexto.Controller.controller import Controller
from MarcaAguaTexto.Model.model import Model
from MarcaAguaTexto.View.view import View

# Main

if __name__ == "__main__":
    model = Model()
    #view = View(model)
    controller = Controller(model)
    view = View(on_submit_callback=controller.receber_dados_submetidos)

    controller.set_view(view)  

    #view.controller = controller  # [Alteração DEV3 - Ligação entre View e Controller]

    print("Chamar iniciar_programa()...")  # Debug Dev2
    controller.iniciar_programa()
    