
temperaturas = []

meses_extenso = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses_extenso[i]}: "))
    temperaturas.append(temperatura)


media_anual = sum(temperaturas) / 12


meses_acima_media = [meses_extenso[i] for i in range(12) if temperaturas[i] >= media_anual]

print(f"A média anual das temperaturas é {media_anual:.2f}°C.")


if len(meses_acima_media) > 0:
    print("A temperatura foi igual ou superior à média anual nos seguintes meses:")
    for mes in meses_acima_media:
        print(mes)
else:
    print("erro")



