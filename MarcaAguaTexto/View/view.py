from MarcaAguaTexto.Model.model import IModel

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

# Interface da classe View
class IView:
    def ativar_boas_vindas(self):
        raise NotImplementedError

    def ativar_rotulo_prompt(self):
        raise NotImplementedError

    def ativar_rotulo_dados(self):
        raise NotImplementedError

    def submeter_dados(self):
        raise NotImplementedError

    def notificar_dados_submetidos(self):
         raise NotImplementedError

    def mostrar_msg_em_curso(self):
        raise NotImplementedError

    def mostrar_msg_sucesso(self):
        raise NotImplementedError

    def mostrar_msg_dados_validos(self):
        raise NotImplementedError

    def mostrar_msg_dados_invalidos(self):
        raise NotImplementedError

    def mostrar_msg_final(self):
        raise NotImplementedError

# Classe View
class View(IView):
    def __init__(self, model: IModel, controller=None, on_submit_callback=None):
        self.model = model
        self.root = tk.Tk()
        print("Janela iniciada")  # Debug Dev2
        self.content_frame = None #Inicializar global em vez de local para que os elementos possam ser adicionados
        self.sidebar_frame = None #Mesma coisa -^
        self.on_submit_callback = on_submit_callback
 
    # TODO Dev #2 - Substituir o print pelo ecrã de boas-vindas/inicial da aplicação
    def ativar_boas_vindas(self):
        self.root.title("Equipa6-Python")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E2E2E")

        # secção para estilos dos widgets
        style = ttk.Style()
        style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Arial", 12))
        style.configure("TText", background="#444444", foreground="white")

        # Painel esquerdo (botoes)
        self.sidebar_frame = tk.Frame(self.root, width=200, bg="#333333")
        self.sidebar_frame.grid(row=0, column=0, rowspan=1, sticky="nsew")

        # Painel direito (conteudo)
        self.content_frame = tk.Frame(self.root, width=400, bg="#2E2E2E")
        self.content_frame.grid(row=0, column=1, sticky="nsew")

        # configuracao do layout em grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1, minsize=200)
        self.root.grid_columnconfigure(1, weight=3, minsize=400)

        # Etiqueta de identificação App
        title_label = ttk.Label(self.sidebar_frame, text="MarcaAguaTexto", font=("Arial", 12, "bold"))
        title_label.pack(pady=(20, 10))

        # Limpa o painel de conteúdo antes de mostrar a tela de boas-vindas
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Ecrã de boas-vindas
        welcome_label = ttk.Label(
            self.content_frame,
            text="Bem-vindo(a) ao MarcaAguaTexto!",
            font=("Arial", 16, "bold"),
            background="#2E2E2E",
            foreground="white"
        )
        welcome_label.pack(pady=(60, 10))

        info_label = ttk.Label(
            self.content_frame,
            text="Esta aplicação permite introduzir uma marca de água não visível ao olho humando em ficheiros de texto.",
            font=("Arial", 12),
            background="#2E2E2E",
            foreground="white",
            justify="center",
            wraplength=360
        )
        info_label.pack(pady=(0, 30))

        start_button = tk.Button(
            self.content_frame,
            text="Começar",
            command=self.mostrar_formulario_principal,
            bg="#808080",
            fg="white",
            width=20,
            height=2
        )
        start_button.pack()

    def mostrar_formulario_principal(self):
        # Limpa o painel de conteúdo e mostra o formulário principal
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.status_label = ttk.Label(self.content_frame, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)
        self.status_label.config(text="Bem-Vind@!")
        self.ativar_rotulo_prompt()
        self.submeter_dados()

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
        self.ativar_rotulo_prompt()    # Elemento de inserção de texto
        print("A inserir elemento2-botao iniciar na janela")  # DEBUG Dev2
        self.submeter_dados()   # Botão de Inicio
        

    def run(self):
        self.root.mainloop()    #TKinter - Manter janela aberta || CHECK -> Funciona, mas verificar se é aqui ou no controller def (iniciar_programa) que se coloca

        print("Fecho de janela")  # DEBUG Dev2

    # TODO Dev #2 - Criar o input visual do texto e número de destinatários
    def ativar_rotulo_prompt(self):
        # Introdução de texto
        label = ttk.Label(self.content_frame, text="Introduza o texto a codificar:")
        label.pack(pady=(20, 5))

        self.text_input = tk.Text(self.content_frame, wrap="word", height=4, width=80, bg="#444444", fg="white", insertbackground="white")
        self.text_input.pack(pady=1, padx=20)

        # Campo para número de destinatários
        num_label = ttk.Label(self.content_frame, text="Número de destinatários:")
        num_label.pack(pady=(10, 2))
        self.num_destinatarios_input = tk.Entry(self.content_frame, width=10, bg="#444444", fg="white", insertbackground="white")
        self.num_destinatarios_input.pack(pady=(0, 10))

    def ativar_rotulo_dados(self):
        # Apresentar o texto e o número de destinatários ao utilizador
        resumo = f"Texto submetido:\n{self.model.texto}\n\nNúmero de destinatários: {self.model.num_destinatarios}"
        # Se já existir um label de resumo, destrua-o antes de criar outro
        if hasattr(self, 'resumo_label') and self.resumo_label.winfo_exists():
            self.resumo_label.destroy()
        self.resumo_label = ttk.Label(
            self.content_frame,
            text=resumo,
            background="#2E2E2E",
            foreground="white",
            font=("Arial", 11),
            justify="left",
            wraplength=360
        )
        self.resumo_label.pack(pady=(10, 10))


    def submeter_dados(self):
        start_button = tk.Button(self.sidebar_frame, text="Iniciar WM", command=self.notificar_dados_submetidos, bg="#808080", fg="white", width=20, height=2)
        start_button.pack(pady=10)

    # ---------------------------------------TESTE de funcionamento do botão || necessário realocar código para o apropriado ->> "command="--------------
    def notificar_dados_submetidos(self):
        """
        Inicia o processo de marca de água no texto.
        Atualização DEV3: Agora chama o Controller para codificar.
        """
        texto = self.text_input.get("1.0", tk.END).strip()
        num_destinatarios = self.num_destinatarios_input.get()
        if not texto:
            self.status_label.config(text="Nada introduzido!")
            return
                
        # Se o callback estiver definido, chama-o
        if self.on_submit_callback:
            self.on_submit_callback(texto, num_destinatarios)

        # DEBUG TEMP DEV3
        print(f"Número de espaços no texto: {sum(linha.count(' ') for linha in self.model.texto)}")

    def mostrar_msg_em_curso(self):
        self.status_label.config(text=f"Operação em curso...")

    def mostrar_msg_sucesso(self):
        self.status_label.config(text=f"Concluído com sucesso.")

    def mostrar_msg_dados_validos(self):
        self.status_label.config(text=f"Os dados submetidos são válidos.")

    def mostrar_msg_dados_invalidos(self, msg_erro):
        self.status_label.config(text=f"{msg_erro}")

    def mostrar_msg_erro_na_codificacao(self):
        self.status_label.config(text=f"Ocorreu um erro na codificação.")

    def mostrar_msg_final(self):
        self.status_label.config(text=f"Programa a encerrar...")
