soma = 0
acima = 0
notas = [0.0]*5
for x in range(5):
    notas[x] = float(input("Digite sua nota :"))

for n in range(5):
    soma = soma + notas[n]
media = soma/len(notas)
print(f"a media da sala foi {media}")

for j in range(5):
    if notas[j] > media:
        acima +=1
print(f"alunos acima da media é {acima}")