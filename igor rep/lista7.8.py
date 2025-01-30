temperaturas = {}


meses_extenso = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]


for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses_extenso[i]}: "))
    temperaturas[meses_extenso[i]] = temperatura


media_anual = sum(temperaturas.values()) / 12


meses_acima_media = [mes for mes, temp in temperaturas.items() if temp >= media_anual]


resultado = {
    "Média Anual": media_anual,
    "Meses Acima da Média Anual": meses_acima_media
}


print("Resultados:")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")


nome_arquivo = input("Digite o nome do arquivo para salvar os resultados (exemplo.txt): ")

with open(nome_arquivo, "w") as arquivo:
    for chave, valor in resultado.items():
        arquivo.write(f"{chave}: {valor}\n")

print(f"Resultados salvos em '{nome_arquivo}' no formato de arquivo de texto.")