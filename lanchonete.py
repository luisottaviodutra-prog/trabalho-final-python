# Função para exibir o cardápio da lanchonete
def exibir_cardapio():
    print("\n==============================")
    print("      CARDÁPIO DA LANCHONETE    ")
    print("==============================")
    print(" [1] X-Burger ....... R$ 15,00")
    print(" [2] X-Salada ....... R$ 18,00")
    print(" [3] Cachorro-Quente  R$ 10,00")
    print(" [4] Batata Frita ... R$ 12,00")
    print(" [5] Refrigerante ... R$  6,00")
    print("==============================\n")

# Função para obter o preço do produto com base no código escolhido
def obter_preco_produto(codigo):
    if codigo == 1:
        return 15.00, "X-Burger"
    elif codigo == 2:
        return 18.00, "X-Salada"
    elif codigo == 3:
        return 10.00, "Cachorro-Quente"
    elif codigo == 4:
        return 12.00, "Batata Frita"
    elif codigo == 5:
        return 6.00, "Refrigerante"
    else:
        return 0.0, ""

# Função para calcular o desconto com base no valor total
def calcular_desconto(valor_total):
    if valor_total < 50.00:
        percentual = 0.0
    elif valor_total < 100.00:
        percentual = 5.0
    else:
        percentual = 10.0
    
    valor_desconto = valor_total * (percentual / 100)
    return percentual, valor_desconto

# Função para validar a forma de pagamento
def obter_forma_pagamento():
    print("\nForma de Pagamento:")
    print(" [1] Dinheiro")
    print(" [2] PIX")
    print(" [3] Cartão")
    
    while True:
        opcao = int(input("Escolha a forma de pagamento (1-3): "))
        if opcao == 1:
            return "Dinheiro"
        elif opcao == 2:
            return "PIX"
        elif opcao == 3:
            return "Cartão"
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")

# Função principal do programa
def main():
    print("Bem-vindo ao Sistema de Atendimento da Lanchonete!")
    
    # Identificação do cliente
    nome_cliente = input("Digite o nome do cliente: ")
    
    total_compra = 0.0
    continuar = "s"
    
    # Repetição dos pedidos
    while continuar.lower() == "s":
        exibir_cardapio()
        
        # Seleção do produto
        codigo_produto = int(input("Digite o código do produto desejado: "))
        
        preco, nome_produto = obter_preco_produto(codigo_produto)
        
        # Validação do produto escolhido
        if preco > 0:
            quantidade = int(input(f"Produto escolhido: {nome_produto}. Digite a quantidade: "))
            
            if quantidade > 0:
                # Cálculo do subtotal
                subtotal = preco * quantidade
                total_compra = total_compra + subtotal
                print(f"Subtotal adicionado: R$ {subtotal:.2f}")
            else:
                print("Quantidade inválida! O pedido não foi adicionado.")
        else:
            print("Código de produto inválido! Tente novamente.")
            
        continuar = input("\nDeseja adicionar mais algum produto? (s/n): ")
        
    # Tratamento caso nenhum produto válido tenha sido comprado
    if total_compra == 0.0:
        print("\nNenhum produto foi comprado. Encerrando o atendimento.")
        return

    # Cálculo dos descontos
    percentual_desconto, valor_desconto = calcular_desconto(total_compra)
    valor_final = total_compra - valor_desconto
    
    # Forma de pagamento
    forma_pagamento = obter_forma_pagamento()
    
    # Resultado final (Resumo da Compra)
    print("\n========================================")
    print("           RESUMO DO ATENDIMENTO        ")
    print("========================================")
    print(f" Cliente: {nome_cliente}")
    print(f" Valor original da compra: R$ {total_compra:.2f}")
    print(f" Desconto aplicado: {percentual_desconto}%")
    print(f" Valor do desconto: R$ {valor_desconto:.2f}")
    print(f" Valor final: R$ {valor_final:.2f}")
    print(f" Forma de pagamento: {forma_pagamento}")
    print("========================================")
    print(" Obrigado pela preferência e volte sempre!")

# Execução do programa
if __name__ == "__main__":
    main()