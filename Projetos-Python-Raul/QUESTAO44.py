lucro_total = 0
qtd_lucro_superior_1000 = 0
qtd_lucro_inferior_200 = 0

contador_acoes = 0

while contador_acoes < 10:
    tipo_acao = input("Digite o tipo de ação: ")
    preco_compra = float(input("Digite o preço de compra da ação: "))
    preco_venda = float(input("Digite o preço de venda da ação: "))

    lucro_acao = preco_venda - preco_compra
    lucro_total += lucro_acao
    contador_acoes += 1

    print(f"Lucro da ação {tipo_acao}: R$ {lucro_acao:.2f}")

    if lucro_acao > 1000:
        qtd_lucro_superior_1000 += 1
    if lucro_acao < 200:
        qtd_lucro_inferior_200 += 1

print(f"Quantidade de ações com lucro superior a R$ 1.000,00: {qtd_lucro_superior_1000}")
print(f"Quantidade de ações com lucro inferior a R$ 200,00: {qtd_lucro_inferior_200}")
print(f"Lucro total da empresa: R$ {lucro_total:.2f}"