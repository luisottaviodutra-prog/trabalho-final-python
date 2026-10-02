#Sistema de Atendimento e Pedidos em Lanchonete

## Identificação
* **Estudante:** Luís Otávio Dutra
* **Disciplina:** Algoritmos e Programação

## Título do Projeto
Sistema Automatizado de Atendimento para Lanchonete

## Breve Descrição do Programa
Este programa foi desenvolvido em Python com o objetivo de substituir o registro manual de pedidos de uma pequena lanchonete[cite: 1, 3]. Ele permite identificar o cliente, apresentar o cardápio, computar quantidades e subtotais, aplicar regras de desconto progressivo, processar o pagamento e exibir um resumo detalhado da compra[cite: 1, 2, 3].

## Principais Funcionalidades Implementadas
* **Identificação do cliente:** Coleta o nome do cliente no início da execução[cite: 2].
* **Cardápio interativo:** Exibe opções de produtos com códigos e preços definidos[cite: 2].
* **Controle de fluxo e repetição:** Utiliza a estrutura `while` para permitir múltiplos pedidos até que o usuário decida finalizar[cite: 2].
* **Validação de entradas:** Trata códigos de produtos e quantidades inválidas de forma segura[cite: 2, 3].
* **Cálculo de descontos:** Aplica descontos automáticos de 5% ou 10% com base no valor total da compra[cite: 2, 3].
* **Seleção de pagamento:** Valida e registra a forma de pagamento escolhida (Dinheiro, PIX ou Cartão)[cite: 3].
* **Organização modular:** Utiliza funções para separar responsabilidades lógicas do código[cite: 3].

## Instruções para Executar o Programa
1. Ter o **Python** instalado no computador
2. Baixe ou clone deste repositório.
3. Abra o terminal ou prompt de comando na pasta onde se encontra o arquivo principal do programa (`main.py`).
4. Executar o comando abaixo:
   ```bash
   python lanchonete.py