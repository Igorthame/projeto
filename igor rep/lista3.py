idades = []
alturas = []

for i in range(1,11):
    print(f"Informações da pessoa {i}:")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura : "))
    idades.append(idade)
    alturas.append(altura)

media_alturas = sum(alturas) / len(alturas)

contador = 0

while i in range(10):
    if idades[i] > 13 and alturas[i] < media_alturas:
        contador += 1

print(f"Quantidade de pessoas com mais de 13 anos e altura inferior à média: {contador}")




