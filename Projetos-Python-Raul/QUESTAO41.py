soma_idades = 0
contador = 0

while contador < 10:
    idade = int(input("Digite uma idade: "))
    soma_idades += idade
    contador += 1

media_idades = soma_idades / 10

print(f"A média das 10 idades digitadas é: {media_idades}")