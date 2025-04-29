nomes= ["joao","carlos","maria","luiza","isabel"]
aluno = input("digite um nome :")
for x in range(len(nomes)):
    if aluno == nomes[x]:
        print(f"achei {aluno} na posição {x}")
else:
    print("nome não encontrado")