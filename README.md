# MarcaAguaTexto

Projeto de simulação empresarial desenvolvido no âmbito da unidade curricular **Laboratório de Desenvolvimento de Software** (Licenciatura em Engenharia Informática, Universidade Aberta – Portugal).

O objetivo deste projeto é desenvolver uma aplicação capaz de introduzir uma marca de água não visível ao olho humando em ficheiros de texto.

---

## 📚 Sobre o Projeto

A aplicação implementa um fluxo básico de manipulação de texto, onde:

- Recebe um texto e o número de destinatários.
- Converte o número em binário de 9 bits.
- Calcula um CRC-8 para validação.
- Codifica o texto original embutindo a marca de água.
- Gera um novo ficheiro de saída com a marca embutida.

O projeto está organizado segundo o padrão **MVC (Model-View-Controller)**:

- **Model**: Gere os dados (texto original, texto codificado, operações de validação e gravação).
- **View**: Responsável pela interação com o utilizador (input/output).
- **Controller**: Faz a ligação entre o Model e a View, coordenando a lógica do programa.

---

## 💪 Tecnologias utilizadas

- Python 3.10+
- Pytest (para testes automatizados)
- CRCMod (para geração de CRC-8)
- tkinter (Python interface)
- Estrutura modular (MVC)

---

## 🚀 Como correr o projeto

1. Clonar o repositório:

```bash
git clone https://github.com/antonina-pereira/MarcaAguaTexto.git
cd MarcaAguaTexto
```

2. Criar e ativar um ambiente virtual:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r MarcaAguaTexto/requirements.txt
pip install pytest
$env:PYTHONPATH = "$PWD\MarcaAguaTexto"
```

3. Executar o programa:

```bash
python -m MarcaAguaTexto.main
```

4. Executar os testes:

```bash
python -m pytest MarcaAguaTexto/tests/
```

---

## 📂 Estrutura do Projeto

```
MarcaAguaTexto/
│
├── Controller/          # Lógica de controlo
│   └── utils/           # Utilitários como CRC
│
├── Model/               # Manipulação de dados (texto e marca de água)
│
├── View/                # Interação com o utilizador (CLI)
│
├── tests/               # Testes automatizados (Pytest)
│
├── Saida/               # Pasta para ficheiros de saída gerados
│
├── Docs/               # Pasta para documentação
│
└── main.py              # Ponto de entrada do programa
```

---

## 🔪 Testes

O projeto inclui testes de:

- Caixa aberta
- Caixa fechada
- Integração de baixo para cima
- Integração de cima para baixo
- Testes de explosão

Todos os testes encontram-se documentados em [`docs/plano_testes.md`](docs/plano_testes.md), onde cada ID corresponde a um comentário associado no respetivo código de testes.

Para correr todos os testes:

```bash
python -m pytest MarcaAguaTexto/tests/
```

---

## 📜 Notas

- A pasta `saida/` é mantida no repositório com um ficheiro `.gitkeep` para garantir a sua presença.
- A pasta `venv/` é ignorada pelo controlo de versões.
- O projeto foi desenvolvido no âmbito da metodologia e-SimProgramming, num ambiente de simulação de empresa onde os estudantes assumem o papel de estagiários recentemente contratados pela empresa fictícia SimProgramming, seguindo práticas profissionais de desenvolvimento colaborativo e aprendizagem baseada em problemas.