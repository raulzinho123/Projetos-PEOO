audiencia_por_canal = {4: 0, 5: 0, 7: 0, 12: 0}


total_pessoas = 0

while True:
    canal = int(input("Digite o número do canal (4, 5, 7 ou 12, ou -1 para sair): "))
    
    if canal == -1:
        break  
    
    if canal in audiencia_por_canal:
        pessoas_assistindo = int(input(f"Digite o número de pessoas assistindo ao canal {canal}: "))
        audiencia_por_canal[canal] += pessoas_assistindo
        total_pessoas += pessoas_assistindo

for canal, audiencia in audiencia_por_canal.items():
    porcentagem = (audiencia / total_pessoas) * 100
    print(f"Canal {canal}: {porcentagem:.2f}% da audiência total")

if total_pessoas == 0:
    print("Nenhum dado de audiência foi inserido.")