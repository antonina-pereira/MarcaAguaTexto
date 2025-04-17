from MarcaAguaTexto.Controller.controller import Controller
from MarcaAguaTexto.Model.model import Model
from MarcaAguaTexto.View.view import View

# Main

if __name__ == "__main__":
    model = Model()
    view = View(model)

    controller = Controller(model, view)

    controller.iniciar_programa()