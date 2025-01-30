import random
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia dinheiro para a vítima?",
    "Já trabalhou com a vítima?"
]


def gerar_respostas_aleatorias():
    return [random.randint(0, 1 ) for _ in range(5)]

num_pessoas = int(input(f"Digite o número de pessoas na simulação :"))

total_respostas_sim = [0] * 5
pergunta_mais_sim = None
pergunta_menos_sim = None
pergunta_mais_cumplices = None
pergunta_menos_cumplices = None
total_cumplices = 0


for i in range(num_pessoas):
    respostas = gerar_respostas_aleatorias()
    total_respostas_sim = [total_respostas_sim[j] + respostas[j] for j in range(5)]
    total_cumplices += respostas.count(1)
    
    if pergunta_mais_sim is None or respostas.count(1) > total_respostas_sim[pergunta_mais_sim]:
       pergunta_mais_sim = respostas.index(1)
    
    if pergunta_menos_sim is None or respostas.count(1) < total_respostas_sim[pergunta_menos_sim]:
      pergunta_menos_sim = respostas.index(1)
    
    if pergunta_mais_cumplices is None or respostas.count(1) > total_cumplices:
      pergunta_mais_cumplices = respostas.index(1)
    
    if pergunta_menos_cumplices is None or respostas.count(1) < total_cumplices:
     pergunta_menos_cumplices = respostas.index(1)

frequencias_relativas = [total_respostas_sim[j] / num_pessoas for j in range(5)]

pergunta_mais_frequente = frequencias_relativas.index(max(frequencias_relativas))
pergunta_menos_frequente = frequencias_relativas.index(min(frequencias_relativas))

print("\nEstatísticas da Simulação:")
for j in range(5):
    print(f"{perguntas[j]} - Frequência Relativa de 'Sim': {frequencias_relativas[j]*100:.2f}%")

print(f"A pergunta com mais respostas 'Sim' foi: {perguntas[pergunta_mais_frequente]}")
print(f"A pergunta com menos respostas 'Sim' foi: {perguntas[pergunta_menos_frequente]}")
print(f"A pergunta mais respondida pelos cúmplices foi: {perguntas[pergunta_mais_cumplices]}")
print(f"A pergunta menos respondida pelos cúmplices foi: {perguntas[pergunta_menos_cumplices]}")
