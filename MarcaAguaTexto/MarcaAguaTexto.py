from MarcaAguaTexto.controller import controller
from MarcaAguaTexto.model import model
from MarcaAguaTexto.view import view

# Main

if __name__ == "__main__":
    model = model.Model()
    view = view.View(model)

    controller = controller.Controller(model, view)

    controller.iniciar_programa()