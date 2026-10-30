# Listas para armazenar o histórico das compras
lista_bruta = []
lista_descontos = []
lista_finais = []

print("=== CAIXA / PDV INICIADO ===")
print("Digite 0 no valor da compra para encerrar e ver o resumo.\n")

# Repetições principal de compras
while True:
    valor_original = float(input("Digite o valor da compra (R$): "))
    
    # Condição de parada do loop
    if valor_original == 0:
        break
        
    idade = int(input("Digite a idade do cliente: "))

    # Validação simples para valores ou idades negativos
    if valor_original < 0 or idade < 0:
        print("Aviso: O valor da compra e a idade não podem ser negativos. Tente novamente.\n")
        continue

    # Regra 1: Desconto por idade (>= 65 anos ganha 20% de desconto)
    if idade >= 65:
        valor_com_desconto_idade = valor_original * 0.8
        desconto_idade = valor_original * 0.2
    else:
        valor_com_desconto_idade = valor_original
        desconto_idade = 0.0

    # Regra 2: Desconto por valor (se o valor já com desconto de idade for > 100, aplica 10% extra)
    if valor_com_desconto_idade > 100.0:
        valor_final = valor_com_desconto_idade * 0.9
        desconto_extra = valor_com_desconto_idade * 0.1
    else:
        valor_final = valor_com_desconto_idade
        desconto_extra = 0.0

    # Soma total dos descontos aplicados nesta compra
    desconto_total_compra = desconto_idade + desconto_extra

    # Exibe o valor final formatado com duas casas decimais
    print(f"Valor final: R$ {valor_final:.2f}\n")

    # Guarda os dados nas listas usando .append()
    lista_bruta.append(valor_original)
    lista_descontos.append(desconto_total_compra)
    lista_finais.append(valor_final)

# Resumo final ao encerrar o programa
print("\n" + "="*30)
print("=== RESUMO DO DIA ===")
print("="*30)

quantidade_compras = len(lista_finais)
print(f"Quantidade de compras registradas: {quantidade_compras}")

if quantidade_compras > 0:
    total_bruto = sum(lista_bruta)
    total_descontos_concedidos = sum(lista_descontos)
    total_final_geral = sum(lista_finais)

    print(f"Total bruto: R$ {total_bruto:.2f}")
    print(f"Total de descontos concedidos: R$ {total_descontos_concedidos:.2f}")
    print(f"Total final: R$ {total_final_geral:.2f}")
else:
    print("Nenhuma compra foi processada.")
print("="*30)