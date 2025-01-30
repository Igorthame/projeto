import json

idades = []
alturas = []


for i in range(1,11):
    print(f"Informações da pessoa {i}:")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura em metros: "))
    idades.append(idade)
    alturas.append(altura)


media_alturas = sum(alturas) / len(alturas)

maior_altura_pessoas = []
menor_altura_pessoas = []

maior_altura = max(alturas)
menor_altura = min(alturas)


for i in range(10):
    if alturas[i] == maior_altura:
        maior_altura_pessoas.append({"idade": idades[i], "altura": alturas[i]})
    if alturas[i] == menor_altura:
        menor_altura_pessoas.append({"idade": idades[i], "altura": alturas[i]})


print("Pessoas com a maior altura:")
for pessoa in maior_altura_pessoas:
    print(f"Idade: {pessoa['idade']}, Altura: {pessoa['altura']}")

print("Pessoas com a menor altura:")
for pessoa in menor_altura_pessoas:
    print(f"Idade: {pessoa['idade']}, Altura: {pessoa['altura']}")

resposta = input("Deseja salvar o resultado em um arquivo JSON? (S/N): ")

if resposta.lower() == 's':
    
    nome_arquivo = input("Digite o nome do arquivo (exemplo.json): ")
    
    resultado_json = {
        "Pessoas com a maior altura": maior_altura_pessoas,
        "Pessoas com a menor altura": menor_altura_pessoas
    }
    
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(resultado_json, arquivo, indent=4)
    
    print(f"Resultado salvo em '{nome_arquivo}' no formato JSON.")
