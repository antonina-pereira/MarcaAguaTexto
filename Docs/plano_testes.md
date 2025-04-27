# Plano de Testes - MarcaAguaTexto

Este documento apresenta o mapeamento completo dos testes realizados para o projeto **MarcaAguaTexto**, desenvolvido no âmbito da unidade curricular **Laboratório de Desenvolvimento de Software** (Licenciatura em Engenharia Informática, Universidade Aberta).

O plano de testes inclui testes de caixa fechada, caixa aberta, integração de cima para baixo, integração de baixo para cima e testes de explosão.

---

## 🔧 Testes Dinâmicos Unitários de Caixa Fechada

| ID    | Criado | Descrição                                           | Dados de Input                          | Resultado Esperado                                   | Notas |
|-------|--------|--------------------------------------------------------|-----------------------------------------|------------------------------------------------------|-------|
| CF001 | ✅ | Verificar mensagem final | Texto e número válidos | View apresenta confirmação no final | Foi testado a apresentação da confirmação após codificação com sucesso |
| CF002 | ✅ | Executar programa com texto válido e 50 destinatários | Texto com >=50 espaços, número=50 | Ficheiros criados com marca de água | Foi testado a geração de vários ficheiros corretamente |
| CF003 | ✅ | Executar programa com texto inválido | Texto sem espaços, número=5 | Mensagem de erro para o utilizador | Foi testado mensagens de erro para texto inválido (ex: sem espaços) |
| CF004 | ❌ | Testar número de destinatários inferior a 1 | Número = 0 | Apresenta erro / bloqueio |   |
| CF005 | ✅ | Validar inserção correta do marcador de início e fim (sequência 511) | Texto válido | Verificar que o binário com sequência de 9 bits de 1 está inserido |   |
| CF006 | ✅ | Validar aplicação correta do CRC-8 | Texto e número válidos | Ficheiros contêm código CRC-8 no fim da codificação |   |
| CF007 | ✅ | Validar codificação correta dos espaços e espaços ininterruptos | Texto e número válidos | Espaços simples são 0, espaços ininterruptos são 1 |   |
| CF008 | ❌ | Gerar ficheiros corretamente para exatamente 510 destinatários | Número = 510 | 510 ficheiros criados com marca de água correta |   |
| CF009 | ❌ | Texto insuficiente para codificação de todos os destinatários | Texto com poucos espaços, número alto | Apresentar erro de codificação |   |

---

## 🔧 Testes Dinâmicos Unitários de Caixa Aberta

| ID    | Criado | Descrição                                           | Dados de Input                          | Resultado Esperado                                   | Notas |
|-------|--------|--------------------------------------------------------|-----------------------------------------|------------------------------------------------------|-------|
| CA001 | ✅ | Validar texto com espaços suficientes | Texto com mais de 100 espaços; número=100 | Retorna True | Validação de número mínimo de espaços foi testada |
| CA002 | ✅ | Validar texto com espaços insuficientes | Texto com menos de 10 espaços; número=10 | Retorna False |   |
| CA003 | ✅ | Validar número de destinatários acima do limite | Texto válido; número=1000 | Retorna False |   |
| CA004 | ✅ | Converter número válido para binário | Número = 42 | Retorna "000101010" |   |
| CA005 | ✅ | Converter número mínimo para binário | Número = 0 | Retorna "000000000" |   |
| CA006 | ✅ | Lançar erro ao converter número inválido (-1) | Número = -1 | Gera erro do tipo ValueError |   |
| CA007 | ✅ | Lançar erro ao converter número inválido (limite++) | Número = limite++ | Gera erro do tipo ValueError |   |
| CA008 | ✅ | Gerar CRC-8 de string binária | Binário = "000101010" | Retorna string de 8 bits (ex: "10101010") | Acho que não errei, isto é 8bits, certo? |
| CA009 | ✅ | Criar e validar ficheiro de saída | Nenhum (só cria o ficheiro) | criar_ficheiro() e validar_ficheiro() retornam True |   |
| CA010 | ✅ | Escrever e validar escrita em ficheiro | Texto com 3 linhas | escrever_ficheiro() e validar_escrita() retornam True |   |
| CA011 | ✅ | Codificar texto com binário válido | Texto com >= 40 espaços, binário de 9 bits | Retorna string com mesmo comprimento |   |
| CA012 | ✅ | Erro ao codificar texto com poucos espaços | Texto com 5 espaços, binário de 9 bits | Gera erro do tipo ValueError |   |
| CA013 | ✅ | Validar dados com texto vazio | texto = [], numero = 5 | Retorna False |   |
| CA014 | ✅ | Validar texto com apenas espaços em branco | Texto com " " (vários espaços seguidos) | Retorna True | Não sei como será suposto reagir, mas assumo que seja para dar erro? AP - Diria que retorna true porque é possível codificar os espaços |
| CA015 | ✅ | Tentar escrever ficheiro sem texto definido no model | model.texto_original = [], depois escrever_ficheiro() | Retorna False ou lança exceção |   |
| CA016 | ❌ | Codificar texto com número de espaços igual ao necessário | Texto com 9 espaços, binário com 9 bits | Retorna texto com todos os espaços substituídos |   |
| CA017 | ✅ | Codificar texto com caracteres especiais | Texto com acentos, emojis, símbolos; número = 5 | Codificação é bem-sucedida ou erro esperado | Garante compatibilidade com UTF-8 |

---

## 🔧 Testes de Integração de Cima para Baixo

| ID    | Criado | Descrição                                           | Dados de Input                          | Resultado Esperado                                   | Notas |
|-------|--------|--------------------------------------------------------|-----------------------------------------|------------------------------------------------------|-------|
| CB001 | ❌ | Chamada ao controller.iniciar_programa() | Texto válido, número=30 | Fluxo completo de codificação executado |   |
| CB002 | ❌ | Controller chama Model e View | Componente Controller inicializa ambos | Ficheiro criado sem exceções |   |
| CB003 | ❌ | Controller gere erro do Model | Texto inválido (poucos espaços) | Mensagem de erro sem crash |   |


---

## 🔧 Testes de Integração de Baixo para Cima

| ID    | Criado | Descrição                                           | Dados de Input                          | Resultado Esperado                                   | Notas |
|-------|--------|--------------------------------------------------------|-----------------------------------------|------------------------------------------------------|-------|
| BC001 | ✅ | Validar dados e criar ficheiro (Model) | Texto com espaços e número viável | Validação = True; ficheiro é criado |   |
| BC002 | ✅ | Escrever texto e validar escrita no ficheiro (Model) | Texto com várias linhas | Escrita e validação retornam True |   |
| BC003 | ✅ | Codificar texto com binário válido (Encoding) | Texto com >= 40 espaços, binário com 9 bits | Codificação retorna string do mesmo comprimento |   |
| BC004 | ✅ | Codificação falha com poucos espaços (Encoding) | Texto com 5 espaços, binário com 9 bits | Gera erro do tipo ValueError |   |
| BC005 | ❌ | Validar dados no Model -> Usar no View | Texto válido, número=20 | View aceita dados para codificação |   |
| BC006 | ❌ | Model retorna True -> Controller executa codificação | Texto válido e número=100 | Codificação binária executada |   |
| BC007 | ❌ | Codificação válida -> Geração do ficheiro final | Binário e CRC válidos | Ficheiro é criado com texto alterado |   |

---

## 🔧 Testes de Explosão (Big Bang)

| ID    | Criado | Descrição                                           | Dados de Input                          | Resultado Esperado                                   | Notas |
|-------|--------|--------------------------------------------------------|-----------------------------------------|------------------------------------------------------|-------|
| EX001 | ❌ | Executar main.py com input completo | Texto com 300 espaços, número=300 | Ficheiro com marca de água criado |   |
| EX002 | ❌ | Injetar falha na View durante execução | Mock impede View de apresentar mensagem | Exceção tratada, aplicação não encerra abruptamente |   |
| EX003 | ❌ | Executar sistema completo com dados reais | Texto realista, número=200 | Texto final com marca embutida |   |
| EX004 | ❌ | Verificar comportamento com erro em ficheiro durante execução global | Texto válido, mas erro ao escrever ficheiro | Erro tratado sem crash |   |

---

## 💡 Notas adicionais

- A criação de ambiente virtual (venv) é recomendada para isolar dependências.
- A execução dos testes pode ser realizada com:

```bash
python -m pytest MarcaAguaTexto/tests/
```