import random


perg = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia dinheiro para a vítima?",
    "Já trabalhou com a vítima?"
]


def gerar_respostas_aleatorias():
    return [random.randint(0, 1) for _ in range(5)]


num_pessoas = int(input("Digite o número de pessoas na simulação (por exemplo, 10): "))

suspeitos = 0
cumplices = 0
assassinos = 0

for i in range(num_pessoas):
    respostas = gerar_respostas_aleatorias()
    print(f"\nRespostas da pessoa {i + 1}:")
    for j in range(5):
        print(f"{perg[j]}: {'Sim' if respostas[j] == 1 else 'Não'}")
    
   
    if respostas.count(1) == 2:
        suspeitos += 1
    elif 3 <= respostas.count(1) <= 4:
        cumplices += 1
    elif respostas.count(1) == 5:
        assassinos += 1

print("\nResultado da simulação:")
print(f"Suspeitos: {suspeitos}")
print(f"Cúmplices: {cumplices}")
print(f"Assassinos: {assassinos}")