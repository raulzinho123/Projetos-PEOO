soma_salarios = 0
maior_idade = float('-inf')
menor_idade = float('inf')
quantidade_mulheres_salario_200 = 0
menor_salario = float('inf')
idade_menor_salario = 0
sexo_menor_salario = ""

contador_idades = 0

while contador_idades < 10:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()
    salario = float(input("Digite o salário: "))

    soma_salarios += salario
    contador_idades += 1

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

    if sexo == 'F' and salario <= 200:
        quantidade_mulheres_salario_200 += 1

    if salario < menor_salario:
        menor_salario = salario
        idade_menor_salario = idade
        sexo_menor_salario = sexo

media_salarios = soma_salarios / 10

print(f"Média dos salários: R$ {media_salarios:.2f}")
print(f"Maior idade: {maior_idade} anos")
print(f"Menor idade: {menor_idade} anos")
print(f"Quantidade de mulheres com salário até R$ 200,00: {quantidade_mulheres_salario_200}")
print(f"Pessoa com menor salário: Idade: {idade_menor_salario} anos, Sexo: {sexo_menor_salario}")