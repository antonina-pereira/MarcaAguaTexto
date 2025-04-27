from MarcaAguaTexto.Model.model import IModel

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import os

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
        self.root = tk.Tk()
        print("Janela iniciada")  # Debug Dev2
        self.content_frame = None #Inicializar global em vez de local para que os elementos possam ser adicionados
        self.sidebar_frame = None #Mesma coisa -^
        #self.ativar_boas_vindas()
 
    # TODO Dev #2 - Substituir o print pelo ecr� de boas-vindas/inicial da aplica��o
    def ativar_boas_vindas(self):
        self.root.title("Equipa6-Python")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E2E2E")

        #secção para estilos dos widgets
        style = ttk.Style()
        style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Arial", 12))
        #style.configure("TButton", background="#808080", foreground="white", font=("Arial", 12)) --> Optei por usar tk pois não assume alguns elementos ttk
        style.configure("TText", background="#444444", foreground="white")

        # Painel esquerdo (botoes)
        self.sidebar_frame = tk.Frame(self.root, width=200, bg="#333333")
        self.sidebar_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")

        # Painel direito (conteudo)
        self.content_frame = tk.Frame(self.root, width=400, bg="#2E2E2E")
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        # configuracao do layout em grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1, minsize=200) #aspect ratio de 25-75
        self.root.grid_columnconfigure(1, weight=3, minsize=400) #aspect ratio de 25-75

        # Etiqueta de identificação App
        title_label = ttk.Label(self.sidebar_frame, text="MarcaAguaTexto", font=("Arial", 12, "bold"))
        title_label.pack(pady=(20, 10))

        # Etiqueta dinâmica para verificação de estado atual
        self.status_label = ttk.Label(self.content_frame, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)
        self.status_label.config(text="Bem-Vind@!")

        print("A inserir elemento1-input texto na janela")  # DEBUG Dev2
        self.rotulo_prompt()    # Elemento de inserção de texto
        print("A inserir elemento2-botao iniciar na janela")  # DEBUG Dev2
        self.submeter_dados()   # Botão de Inicio
        

    def run(self):
        self.root.mainloop()    #TKinter - Manter janela aberta || CHECK -> Funciona, mas verificar se é aqui ou no controller def (iniciar_programa) que se coloca

        print("Fecho de janela")  # DEBUG Dev2

    # TODO Dev #2 - Criar o input visual do texto e n�mero de destinat�rios
    def rotulo_prompt(self):
        # Introdução de texto
        label = ttk.Label(self.content_frame, text="Introduza o texto a codificar:")
        label.pack(pady=(20, 5))

        self.text_input = tk.Text(self.content_frame, wrap="word", height=4, width=80, bg="#444444", fg="white", insertbackground="white")
        self.text_input.pack(pady=1, padx=20)


    # TODO Dev #2 - Guardar os dados introduzidos pelo utilizador 
    # <<<----- Tenho dúvidas na implementação, é para guardar em memória? ficheiro.txt? Confundi com a função acima e fiz tudo na mesma função?
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
        start_button = tk.Button(self.sidebar_frame, text="Iniciar WM", command=self.start_watermarking, bg="#808080", fg="white", width=20, height=2)
        start_button.pack(pady=10)

    # ---------------------------------------TESTE de funcionamento do botão || necessário realocar código para o apropriado ->> "command="--------------
    def start_watermarking(self):
        """Gerir o processo de watermarking (para ser implementado)."""
        text = self.text_input.get("1.0", tk.END).strip()  # Input do texto a codificar
        if not text:
            self.status_label.config(text="Nada introduzido!")
            return
        
        self.status_label.config(text=f"WM iniciado para: {text}")
        # TODO: Chamar a função respetiva.
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    def dados_submetidos(self):
        self.status_label.config(text=f"Dados submetidos!") # Assumo que isto será mensagem uma vez que existe submeter_dados 

    def mensagem_em_curso(self):
        self.status_label.config(text=f"Operação em curso...")

    def validar_dados(self):
        pass

    def codificacao_terminou(self):
        self.status_label.config(text=f"Codificação concluída.")

    def mensagem_sucesso(self):
        self.status_label.config(text=f"Concluído com sucesso.")

    def mensagem_dados_validos(self):
        self.status_label.config(text=f"Os dados submetidos são válidos.")

    def mensagem_dados_invalidos(self):
        self.status_label.config(text=f"Os dados submetidos são inválidos!!") # {text} Adicionar código de erro aqui? 
