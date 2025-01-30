import xml.etree.ElementTree as ET


idades = []
alturas = []


for i in range(1, 11):
    print(f"Informações da pessoa {i}:")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura em metros: "))
    idades.append(idade)
    alturas.append(altura)


media_alturas = sum(alturas) / len(alturas)


contador = 0


for i in range(10):
    if idades[i] > 13 and alturas[i] < media_alturas:
        contador += 1


print(f"Quantidade de pessoas com mais de 13 anos e altura inferior à média: {contador}")

#
resposta = input("Deseja salvar o resultado em um arquivo XML? (S/N): ")

if resposta.lower() == 's':
    
    nome_arquivo = input("Digite o nome do arquivo (exemplo.xml): ")
    
    
    resultado_xml = ET.Element("resultado")
    ET.SubElement(resultado_xml, "quantidade").text = str(contador)
    
   
    tree = ET.ElementTree(resultado_xml)
    tree.write(nome_arquivo)
    
    print(f"Resultado salvo em '{nome_arquivo}' no formato XML.")